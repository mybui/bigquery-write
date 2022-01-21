import json

from flask import Flask

from bq_client import BigQueryClient
from bq_config import *
from elq_client import ElqClient
from settings import *

if LOG == "remote":
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


app = Flask(__name__)


@app.route("/")
def status():
    bq_client = BigQueryClient()
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)

    if bq_client and elq_client:
        app.logger.info("Service is healthy and alive.")
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False}), 400, {'ContentType': 'application/json'}


def daily_load_other_data(bq_client, parameters):
    output = list()
    for item in parameters:
        table = list(item.keys())[0]
        delete_job = bq_client.delete_selected_data(data=item[table]["data"], table=table,
                                                    unique_field=item[table]["unique_field"])
        if delete_job or delete_job is None:
            insert_job = bq_client.insert_data(data=item[table]["data"], table=table, schema=item[table]["schema"])
            if insert_job or insert_job is None:
                output.append({table: True})
            else:
                output.append({table: False})
        else:
            output.append({table: False})
    return output


def daily_load_contact_time_series_helper(bq_client, parameters):
    output = list()
    for item in parameters:
        table = list(item.keys())[0]
        insert_job = bq_client.insert_data(data=item[table]["data"], table=table, schema=item[table]["schema"])
        if insert_job or insert_job is None:
            output.append({table: True})
        else:
            output.append({table: False})
    return output


def historical_load_all_data(bq_client, parameters):
    output = list()
    for item in parameters:
        table = list(item.keys())[0]
        insert_job = bq_client.insert_data(data=item[table]["data"], table=table, schema=item[table]["schema"])
        if insert_job or insert_job is None:
            output.append({table: True})
        else:
            output.append({table: False})
    return output


@app.route("/contact")
def daily_load_contact():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    contacts = elq_client.export_contacts()
    parameters = [
        {
            "contact": {
                "data": contacts,
                "unique_field": "ContactID",
                "schema": contact_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/contact_time_series")
def daily_load_contact_time_series():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    contacts = elq_client.export_contact_time_series()
    parameters = [
        {
            "contact_time_series": {
                "data": contacts,
                "unique_field": "ContactID",
                "schema": contact_time_series_schema
            }
        }
    ]
    output = daily_load_contact_time_series_helper(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/account")
def daily_load_account():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    accounts = elq_client.export_accounts(first_run=True)
    parameters = [
        {
            "account": {
                "data": accounts,
                "unique_field": "CompanyID",
                "schema": account_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/activities/email_open")
def daily_load_activities_email_open():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    email_open = elq_client.export_activities(type="EmailOpen")
    parameters = [
        {
            "email_open": {
                "data": email_open,
                "unique_field": "ActivityId",
                "schema": email_open_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/activities/email_clickthrough")
def daily_load_activities_email_clickthrough():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    email_clickthrough = elq_client.export_activities(type="EmailClickthrough")
    parameters = [
        {
            "email_clickthrough": {
                "data": email_clickthrough,
                "unique_field": "ActivityId",
                "schema": email_clickthrough_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/activities/email_send")
def daily_load_activities_email_send():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    email_send = elq_client.export_activities(type="EmailSend")
    parameters = [
        {
            "email_send": {
                "data": email_send,
                "unique_field": "ActivityId",
                "schema": email_send_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/activities/subscribe")
def daily_load_activities_subscribe():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    subscribe = elq_client.export_activities(type="Subscribe")
    unsubscribe = elq_client.export_activities(type="Unsubscribe")
    parameters = [
        {
            "subscribe": {
                "data": subscribe,
                "unique_field": "ActivityId",
                "schema": subscribe_schema
            }
        },
        {
            "unsubscribe": {
                "data": unsubscribe,
                "unique_field": "ActivityId",
                "schema": unsubscribe_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/activities/other")
def daily_load_activities_other():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    form_submit = elq_client.export_activities(type="FormSubmit")
    bounceback = elq_client.export_activities(type="Bounceback")
    parameters = [
        {
            "form_submit": {
                "data": form_submit,
                "unique_field": "ActivityId",
                "schema": form_submit_schema
            }
        },
        {
            "bounceback": {
                "data": bounceback,
                "unique_field": "ActivityId",
                "schema": bounceback_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/activities/webvisit")
def daily_load_activities_webvisit():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    web_visit = elq_client.export_activities(type="WebVisit")
    parameters = [
        {
            "web_visit": {
                "data": web_visit,
                "unique_field": "ActivityId",
                "schema": web_visit_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/activities/pageview")
def daily_load_activities_pageview():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    page_view = elq_client.export_activities(type="PageView")
    parameters = [
        {
            "page_view": {
                "data": page_view,
                "unique_field": "ActivityId",
                "schema": page_view_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/assets")
def daily_load_assets():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    campaigns = elq_client.export_assets(type="campaigns")
    forms = elq_client.export_assets(type="forms")
    landing_pages = elq_client.export_assets(type="landingPages")
    emails = elq_client.export_assets(type="emails")
    email_groups = elq_client.export_assets(type="email/groups")
    parameters = [
        {
            "campaigns": {
                "data": campaigns,
                "unique_field": "id",
                "schema": campaigns_schema
            }
        },
        {
            "forms": {
                "data": forms,
                "unique_field": "id",
                "schema": forms_schema
            }
        },
        {
            "landing_pages": {
                "data": landing_pages,
                "unique_field": "id",
                "schema": landing_pages_schema
            }
        },
        {
            "emails": {
                "data": emails,
                "unique_field": "id",
                "schema": emails_schema
            }
        },
        {
            "email_groups": {
                "data": email_groups,
                "unique_field": "id",
                "schema": email_groups_schema
            }
        },
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


@app.route("/cdo")
def daily_load_cdo():
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)
    cdo_form_reporting_for_campaign_dashboard = elq_client.export_cdo()
    parameters = [
        {
            "cdo_form_reporting_for_campaign_dashboard": {
                "data": cdo_form_reporting_for_campaign_dashboard,
                "unique_field": "id",
                "schema": cdo_form_reporting_for_campaign_dashboard_schema
            }
        }
    ]
    output = daily_load_other_data(bq_client=BigQueryClient(), parameters=parameters)
    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


# run this only locally because it takes time
# before running, delete all data from all tables
# to avoid duplicates (in the simplest way, there are other more complicated ways)
@app.route("/historical_load")
def historical_load():
    bq_client = BigQueryClient()
    elq_client = ElqClient(username=ELQ_USER, password=ELQ_PASSWORD, base_url=ELQ_BASE_URL)

    contacts = elq_client.export_contacts(first_run=True)
    contact_time_series = elq_client.export_contact_time_series(first_run=True)
    accounts = elq_client.export_accounts(first_run=True)
    email_open = elq_client.export_activities(type="EmailOpen", first_run=True)
    email_clickthrough = elq_client.export_activities(type="EmailClickthrough", first_run=True)
    email_send = elq_client.export_activities(type="EmailSend", first_run=True)
    form_submit = elq_client.export_activities(type="FormSubmit", first_run=True)
    subscribe = elq_client.export_activities(type="Subscribe", first_run=True)
    unsubscribe = elq_client.export_activities(type="Unsubscribe", first_run=True)
    web_visit = elq_client.export_activities(type="WebVisit", first_run=True)
    page_view = elq_client.export_activities(type="PageView", first_run=True)
    bounceback = elq_client.export_activities(type="Bounceback", first_run=True)
    campaigns = elq_client.export_assets(type="campaigns", first_run=True)
    forms = elq_client.export_assets(type="forms", first_run=True)
    landing_pages = elq_client.export_assets(type="landingPages", first_run=True)
    emails = elq_client.export_assets(type="emails", first_run=True)
    email_groups = elq_client.export_assets(type="email/groups", first_run=True)
    cdo_form_reporting_for_campaign_dashboard = elq_client.export_cdo(first_run=True)

    output = list()

    activity_parameters = [
        {
            "email_open": {
                "data": email_open,
                "unique_field": "ActivityId",
                "schema": email_open_schema
            }
        },
        {
            "email_clickthrough": {
                "data": email_clickthrough,
                "unique_field": "ActivityId",
                "schema": email_clickthrough_schema
            }
        },
        {
            "email_send": {
                "data": email_send,
                "unique_field": "ActivityId",
                "schema": email_send_schema
            }
        },
        {
            "form_submit": {
                "data": form_submit,
                "unique_field": "ActivityId",
                "schema": form_submit_schema
            }
        },
        {
            "subscribe": {
                "data": subscribe,
                "unique_field": "ActivityId",
                "schema": subscribe_schema
            }
        },
        {
            "unsubscribe": {
                "data": unsubscribe,
                "unique_field": "ActivityId",
                "schema": unsubscribe_schema
            }
        },
        {
            "web_visit": {
                "data": web_visit,
                "unique_field": "ActivityId",
                "schema": web_visit_schema
            }
        },
        {
            "page_view": {
                "data": page_view,
                "unique_field": "ActivityId",
                "schema": page_view_schema
            }
        },
        {
            "bounceback": {
                "data": bounceback,
                "unique_field": "ActivityId",
                "schema": bounceback_schema
            }
        }
    ]
    output += historical_load_all_data(bq_client=bq_client, parameters=activity_parameters)

    other_parameters = [
        {
            "contact": {
                "data": contacts,
                "unique_field": "ContactID",
                "schema": contact_schema
            }
        },
        {
            "contact_time_series": {
                "data": contact_time_series,
                "unique_field": "ContactID",
                "schema": contact_time_series_schema
            }
        },
        {
            "account": {
                "data": accounts,
                "unique_field": "CompanyID",
                "schema": account_schema
            }
        },
        {
            "campaigns": {
                "data": campaigns,
                "unique_field": "id",
                "schema": campaigns_schema
            }
        },
        {
            "forms": {
                "data": forms,
                "unique_field": "id",
                "schema": forms_schema
            }
        },
        {
            "landing_pages": {
                "data": landing_pages,
                "unique_field": "id",
                "schema": landing_pages_schema
            }
        },
        {
            "emails": {
                "data": emails,
                "unique_field": "id",
                "schema": emails_schema
            }
        },
        {
            "email_groups": {
                "data": email_groups,
                "unique_field": "id",
                "schema": email_groups_schema
            }
        },
    ]
    output += historical_load_all_data(bq_client=bq_client, parameters=other_parameters)

    cdo_parameters = [
        {
            "cdo_form_reporting_for_campaign_dashboard": {
                "data": cdo_form_reporting_for_campaign_dashboard,
                "unique_field": "id",
                "schema": cdo_form_reporting_for_campaign_dashboard_schema
            }
        }
    ]
    output += historical_load_all_data(bq_client=bq_client, parameters=cdo_parameters)

    response = list()
    for table in output:
        for value in table.values():
            response.append(value)

    if all(response):
        return json.dumps({"success": True,
                           "debug": output}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False,
                       "debug": output}), 400, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(PORT))
