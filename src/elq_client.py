from datetime import datetime, timedelta

from dea.bulk.api import BulkClient
from dea.bulk.definitions import ExportDefinition
from dea.rest.api.cdo import RestCdoClient
from requests.auth import HTTPBasicAuth

from datetime import datetime

from elq_config import *


class ElqClient:
    def __init__(self, username, password, base_url):
        self.bulk_client = BulkClient(auth=HTTPBasicAuth(username=username, password=password), base_url=base_url)
        self.rest_client = RestCdoClient(auth=HTTPBasicAuth(username=username, password=password), base_url=base_url)

    def get_last_24_hours_date_time(self):
        past = datetime.utcnow() - timedelta(hours=24)
        date_from = str(past.date()) + " " + str(past.time()).split(".")[0]
        return date_from

    def get_last_12_months_date_time(self):
        past = datetime.utcnow() - timedelta(days=365)
        date_from = str(past.date()) + " " + str(past.time()).split(".")[0]
        return date_from

    def export_activities(self, type, first_run=False):
        if type in activity_export_def.keys():
            if first_run:
                past_time = self.get_last_12_months_date_time()
            else:
                past_time = self.get_last_24_hours_date_time()
            filter = "'{0}'='{1}' AND '{2}'>'{3}'".format("{{Activity.Type}}", type, "{{Activity.CreatedAt}}", past_time)
            export_def = ExportDefinition(name="{0} Activity Export".format(type),
                                          fields=activity_export_def[type],
                                          filter=filter)
            activities = list(self.bulk_client.bulk_activities.exports.create_export(export_def=export_def,
                                                                                     delete_export_on_close=True,
                                                                                     sync_limit=50000))
            if activities:
                for activity in activities:
                    for item in activity:
                        if not activity[item]:
                            activity[item] = None
                return activities
            else:
                return None
        return None

    def export_contacts(self, first_run=False):
        if first_run:
            export_def = ExportDefinition(name="Contact Export", fields=contact_export_def)
            contacts = list(self.bulk_client.bulk_contacts.exports.create_export(export_def=export_def,
                                                                                 delete_export_on_close=True,
                                                                                 sync_limit=50000))
        else:
            past_time = self.get_last_24_hours_date_time()
            filter = "'{0}'>'{1}'".format("{{Contact.Field(C_DateModified)}}", past_time)
            export_def = ExportDefinition(name="Contact Export", fields=contact_export_def, filter=filter)
            contacts = list(self.bulk_client.bulk_contacts.exports.create_export(export_def=export_def,
                                                                                 delete_export_on_close=True,
                                                                                 sync_limit=50000))
        if contacts:
            for contact in contacts:
                for item in contact:
                    if not contact[item]:
                        contact[item] = None
            return contacts
        else:
            return None

    def export_contact_time_series(self, first_run=False):
        if first_run:
            export_def = ExportDefinition(name="Contact Time Series Export", fields=contact_time_series_export_def)
            contacts = list(self.bulk_client.bulk_contacts.exports.create_export(export_def=export_def,
                                                                                 delete_export_on_close=True,
                                                                                 sync_limit=50000))
        else:
            past_time = self.get_last_24_hours_date_time()
            filter = "'{0}'>'{1}'".format("{{Contact.Field(C_DateModified)}}", past_time)
            export_def = ExportDefinition(name="Contact Time Series Export", fields=contact_time_series_export_def,
                                          filter=filter)
            contacts = list(self.bulk_client.bulk_contacts.exports.create_export(export_def=export_def,
                                                                                 delete_export_on_close=True,
                                                                                 sync_limit=50000))
        if contacts:
            for contact in contacts:
                for item in contact:
                    if not contact[item]:
                        contact[item] = None
            return contacts
        else:
            return None

    def export_accounts(self, first_run=False):
        if first_run:
            export_def = ExportDefinition(name="Account Export", fields=account_export_def)
            accounts = list(self.bulk_client.bulk_accounts.exports.create_export(export_def=export_def,
                                                                                 delete_export_on_close=True,
                                                                                 sync_limit=50000))
        else:
            past_time = self.get_last_24_hours_date_time()
            filter = "'{0}'>'{1}'".format("{{Account.Field(M_DateModified)}}", past_time)
            export_def = ExportDefinition(name="Account Export", fields=account_export_def, filter=filter)
            accounts = list(self.bulk_client.bulk_accounts.exports.create_export(export_def=export_def,
                                                                                 delete_export_on_close=True,
                                                                                 sync_limit=50000))
        if accounts:
            for account in accounts:
                for item in account:
                    if not account[item]:
                        account[item] = None
            return accounts
        else:
            return None

    def export_assets(self, type, first_run=False):
        if type in ["campaigns", "forms", "landingPages", "emails", "email/groups"]:
            if first_run:
                past_time = None
            else:
                past_time = self.get_last_24_hours_date_time()

            if past_time:
                # set depth = partial for emails to get info on email group id
                if type == "emails":
                    assets = list(self.rest_client.get(self.rest_client.rest_url_for(path="assets/emails?depth=partial&search=updatedAt>{0}".format(past_time), version="2.0"))["elements"])
                else:
                    filter = "?search=updatedAt>'{0}'".format(past_time)
                    assets = list(self.rest_client.get(self.rest_client.rest_url_for(path="assets/{0}{1}".format(type, filter), version="2.0"))["elements"])
            else:
                if type == "emails":
                    assets = list(self.rest_client.get(self.rest_client.rest_url_for(path="assets/emails?depth=partial", version="2.0"))["elements"])
                else:
                    assets = list(self.rest_client.get(self.rest_client.rest_url_for(path="assets/{0}".format(type), version="2.0"))["elements"])

            permitted_fields = ["id", "currentStatus", "createdAt", "name", "updatedAt", "archived", "subject", "endAt",
                                "startAt", "emailGroupId", "campaignCategory", "isEmailMarketingCampaign", "htmlName",
                                "isResponsive", "description"]
            time_fields = ["createdAt", "updatedAt", "endAt", "startAt"]
            if assets:
                for asset in assets:
                    all_fields = list(asset.keys())
                    extra_fields = [key for key in all_fields if key not in permitted_fields]
                    for time_key in time_fields:
                        timestamp_value = asset.get(time_key, None)
                        if timestamp_value:
                            asset[time_key] = datetime.fromtimestamp(int(timestamp_value)).strftime("%Y-%m-%dT%H:%M:%S")
                        else:
                            asset[time_key] = None
                    for key in extra_fields:
                        asset.pop(key, None)
                    for item in asset:
                        if not asset[item]:
                            asset[item] = None
                return assets
        return None

    def export_cdo(self, first_run=False):
        if first_run:
            export_def = ExportDefinition(name="CDO 6 Export", fields=cdo_export_def, parent_id=cdo_id)
            cdo = list(self.bulk_client.bulk_cdo.exports.create_export(parent_id=cdo_id, export_def=export_def,
                                                                       delete_export_on_close=True, sync_limit=50000))
        else:
            past_time = self.get_last_24_hours_date_time()
            filter = "'{0}'>'{1}'".format("{{CustomObject[6].UpdatedAt}}", past_time)
            export_def = ExportDefinition(name="CDO 6 Export", fields=cdo_export_def, parent_id=cdo_id, filter=filter)
            cdo = list(self.bulk_client.bulk_cdo.exports.create_export(parent_id=cdo_id, export_def=export_def,
                                                                       delete_export_on_close=True, sync_limit=50000))
        if cdo:
            for record in cdo:
                for item in record:
                    if not record[item]:
                        record[item] = None
            return cdo
        else:
            return None

