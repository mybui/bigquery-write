import json

import pandas
from google.cloud import bigquery

import settings

if settings.LOG == "remote":
    import google.cloud.logging

    client = google.cloud.logging.Client()
    client.get_default_handler()
    client.setup_logging()

    import logging
else:
    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )


class BigQueryClient(object):
    def __init__(self):
        self.bq_client = bigquery.Client()

    def delete_selected_data(self, data, table, unique_field):
        if data:
            table_id = f"{settings.GOOGLE_CLOUD_PROJECT}.{settings.GOOGLE_CLOUD_DATASET}.{table}"
            if len(data) >= 1:
                values_from_eloqua_export = [item.get(unique_field, None) for item in data]
            else:
                logging.warning(
                    "----- WARNING ----- No row to delete for upcoming insert table {0}".format(str.title(table)))
                return None
            values_in_bq = list(self.bq_client.query(f"SELECT {unique_field} FROM `{table_id}`;").result())
            values_to_delete_in_bq = [item[0] for item in values_in_bq if item[0] in values_from_eloqua_export]

            if values_to_delete_in_bq:
                condition_string = "("
                for value in values_to_delete_in_bq:
                    condition_string += "'"
                    condition_string += str(value)
                    condition_string += "', "
                condition_string = condition_string[:-2]
                condition_string += ")"

                try:
                    delete_job = self.bq_client.query(
                        f"DELETE FROM `{table_id}` WHERE {unique_field} IN {condition_string};")
                    if delete_job:
                        logging.debug(
                            "----- SUCCESS ----- Delete existing rows for upcoming insert table {0}: {1} rows".format(
                                str.title(table),
                                len(values_to_delete_in_bq)))
                        return True
                    else:
                        logging.error(
                            "----- ERROR ----- Delete existing rows for upcoming insert table {0}: Unknown error. Please debug locally.".format(
                                str.title(table)))
                        return False
                except Exception as e:
                    logging.error(
                        "----- ERROR ----- Delete existing rows for upcoming insert table {0}: {1}".format(str.title(table),
                                                                                                           e))
                    return False
            logging.warning("----- WARNING ----- No row to delete for upcoming insert table {0}".format(str.title(table)))
            return None
        logging.warning("----- WARNING ----- No row to delete for upcoming insert table {0}".format(str.title(table)))
        return None

    def insert_data(self, data, table, schema):
        if data:
            table_id = f"{settings.GOOGLE_CLOUD_PROJECT}.{settings.GOOGLE_CLOUD_DATASET}.{table}"
            data_df = pandas.DataFrame(data)
            data_json = json.loads(data_df.to_json(orient="records"))
            job_config_write = bigquery.LoadJobConfig(
                write_disposition=getattr(bigquery.WriteDisposition, "WRITE_APPEND"),
                source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
                schema=schema
            )
            try:
                load_job = self.bq_client.load_table_from_json(data_json, table_id, job_config=job_config_write)
                if load_job.result():
                    logging.debug(
                        "----- SUCCESS ----- Insert to table {0}: {1} rows".format(str.title(table), len(data)))
                    return True
                logging.error("----- ERROR ----- Insert to table {0}: Unknown error. Please debug locally.".format(
                    str.title(table)))
                return False
            except Exception as e:
                logging.error("----- ERROR ----- Insert to table {0}: {1}".format(str.title(table), e))
                return False
        logging.warning("----- WARNING ----- No row to insert to table {0}".format(str.title(table)))
        return None
