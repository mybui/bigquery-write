contact_schema = [
    {
        "name": "ContactID",
        "type": "STRING"
    },
    {
        "name": "Company",
        "type": "STRING"
    },
    {
        "name": "City",
        "type": "STRING"
    },
    {
        "name": "Country",
        "type": "STRING"
    },
    {
        "name": "Title",
        "type": "STRING"
    },
    {
        "name": "CreatedAt",
        "type": "DATETIME"
    },
    {
        "name": "UpdatedAt",
        "type": "DATETIME"
    },
    {
        "name": "Industry",
        "type": "STRING"
    },
    {
        "name": "AnnualRevenue",
        "type": "STRING"
    },
    {
        "name": "EmailDomain",
        "type": "STRING"
    },
    {
        "name": "MarketingPermission",
        "type": "STRING"
    },
    {
        "name": "MarketingPermissionDate",
        "type": "DATETIME"
    }
]

contact_time_series_schema = [
    {
        "name": "ContactID",
        "type": "STRING"
    },
    {
        "name": "Company",
        "type": "STRING"
    },
    {
        "name": "City",
        "type": "STRING"
    },
    {
        "name": "Country",
        "type": "STRING"
    },
    {
        "name": "Title",
        "type": "STRING"
    },
    {
        "name": "CreatedAt",
        "type": "DATETIME"
    },
    {
        "name": "UpdatedAt",
        "type": "DATETIME"
    },
    {
        "name": "Industry",
        "type": "STRING"
    },
    {
        "name": "AnnualRevenue",
        "type": "STRING"
    },
    {
        "name": "EmailDomain",
        "type": "STRING"
    },
    {
        "name": "MarketingPermission",
        "type": "STRING"
    },
    {
        "name": "MarketingPermissionDate",
        "type": "DATETIME"
    },
    {
        "name": "LeadRating",
        "type": "STRING"
    }
]

account_schema = [
    {
        "name": "CompanyID",
        "type": "STRING"
    },
    {
        "name": "Company",
        "type": "STRING"
    },
    {
        "name": "Country",
        "type": "STRING"
    },
    {
        "name": "Address",
        "type": "STRING"
    },
    {
        "name": "City",
        "type": "STRING"
    },
    {
        "name": "StateOrProvince",
        "type": "STRING"
    },
    {
        "name": "ZipCode",
        "type": "STRING"
    },
    {
        "name": "BusinessPhone",
        "type": "STRING"
    },
    {
        "name": "CreatedAt",
        "type": "DATETIME"
    },
    {
        "name": "UpdatedAt",
        "type": "DATETIME"
    }
]

email_open_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "VisitorId",
        "type": "STRING"
    },
    {
        "name": "AssetType",
        "type": "STRING"
    },
    {
        "name": "AssetName",
        "type": "STRING"
    },
    {
        "name": "AssetId",
        "type": "STRING"
    },
    {
        "name": "VisitorExternalId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    },
    {
        "name": "EmailSendType",
        "type": "STRING"
    }
]

email_clickthrough_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "VisitorId",
        "type": "STRING"
    },
    {
        "name": "AssetType",
        "type": "STRING"
    },
    {
        "name": "AssetName",
        "type": "STRING"
    },
    {
        "name": "AssetId",
        "type": "STRING"
    },
    {
        "name": "VisitorExternalId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    },
    {
        "name": "EmailSendType",
        "type": "STRING"
    }
]

email_send_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "AssetType",
        "type": "STRING"
    },
    {
        "name": "AssetName",
        "type": "STRING"
    },
    {
        "name": "AssetId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    },
    {
        "name": "EmailSendType",
        "type": "STRING"
    }
]

form_submit_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "VisitorId",
        "type": "STRING"
    },
    {
        "name": "AssetType",
        "type": "STRING"
    },
    {
        "name": "AssetName",
        "type": "STRING"
    },
    {
        "name": "AssetId",
        "type": "STRING"
    },
    {
        "name": "VisitorExternalId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    }
]

subscribe_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "AssetType",
        "type": "STRING"
    },
    {
        "name": "AssetName",
        "type": "STRING"
    },
    {
        "name": "AssetId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    }
]

unsubscribe_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "AssetType",
        "type": "STRING"
    },
    {
        "name": "AssetName",
        "type": "STRING"
    },
    {
        "name": "AssetId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    }
]

web_visit_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "VisitorId",
        "type": "STRING"
    },
    {
        "name": "VisitorExternalId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    },
    {
        "name": "Duration",
        "type": "STRING"
    },
    {
        "name": "NumberOfPages",
        "type": "STRING"
    },
    {
        "name": "ReferrerUrl",
        "type": "STRING"
    },
    {
        "name": "FirstPageViewUrl",
        "type": "STRING"
    }
]

page_view_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "VisitorId",
        "type": "STRING"
    },
    {
        "name": "VisitorExternalId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    },
    {
        "name": "ReferrerUrl",
        "type": "STRING"
    },
    {
        "name": "Url",
        "type": "STRING"
    },
    {
        "name": "WebVisitId",
        "type": "STRING"
    }
]

bounceback_schema = [
    {
        "name": "ActivityId",
        "type": "STRING"
    },
    {
        "name": "ContactId",
        "type": "STRING"
    },
    {
        "name": "ActivityType",
        "type": "STRING"
    },
    {
        "name": "ActivityDate",
        "type": "DATETIME"
    },
    {
        "name": "AssetType",
        "type": "STRING"
    },
    {
        "name": "AssetName",
        "type": "STRING"
    },
    {
        "name": "AssetId",
        "type": "STRING"
    },
    {
        "name": "CampaignId",
        "type": "STRING"
    },
    {
        "name": "ExternalId",
        "type": "STRING"
    },
    {
        "name": "SmtpErrorCode",
        "type": "STRING"
    },
    {
        "name": "SmtpStatusCode",
        "type": "STRING"
    },
    {
        "name": "SmtpMessage",
        "type": "STRING"
    }
]

campaigns_schema = [
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "currentStatus",
        "type": "STRING"
    },
    {
        "name": "createdAt",
        "type": "DATETIME"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "updatedAt",
        "type": "DATETIME"
    },
    {
        "name": "campaignCategory",
        "type": "STRING"
    },
    {
        "name": "endAt",
        "type": "DATETIME"
    },
    {
        "name": "isEmailMarketingCampaign",
        "type": "STRING"
    },
    {
        "name": "startAt",
        "type": "DATETIME"
    }
]

forms_schema = [
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "currentStatus",
        "type": "STRING"
    },
    {
        "name": "createdAt",
        "type": "DATETIME"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "updatedAt",
        "type": "DATETIME"
    },
    {
        "name": "archived",
        "type": "STRING"
    },
    {
        "name": "htmlName",
        "type": "STRING"
    },
    {
        "name": "isResponsive",
        "type": "STRING"
    },
    {
        "name": "endAt",
        "type": "DATETIME"
    },
    {
        "name": "startAt",
        "type": "DATETIME"
    }
]

landing_pages_schema = [
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "currentStatus",
        "type": "STRING"
    },
    {
        "name": "createdAt",
        "type": "DATETIME"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "updatedAt",
        "type": "DATETIME"
    },
    {
        "name": "endAt",
        "type": "DATETIME"
    },
    {
        "name": "startAt",
        "type": "DATETIME"
    }
]

emails_schema = [
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "currentStatus",
        "type": "STRING"
    },
    {
        "name": "createdAt",
        "type": "DATETIME"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "emailGroupId",
        "type": "STRING"
    },
    {
        "name": "updatedAt",
        "type": "DATETIME"
    },
    {
        "name": "archived",
        "type": "STRING"
    },
    {
        "name": "subject",
        "type": "STRING"
    },
    {
        "name": "endAt",
        "type": "DATETIME"
    },
    {
        "name": "startAt",
        "type": "DATETIME"
    }
]

email_groups_schema = [
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "createdAt",
        "type": "DATETIME"
    },
    {
        "name": "name",
        "type": "STRING"
    },
    {
        "name": "description",
        "type": "STRING"
    },
    {
        "name": "updatedAt",
        "type": "DATETIME"
    },
    {
        "name": "endAt",
        "type": "DATETIME"
    },
    {
        "name": "startAt",
        "type": "DATETIME"
    }
]

cdo_form_reporting_for_campaign_dashboard_schema = [
    {
        "name": "id",
        "type": "STRING"
    },
    {
        "name": "campaignType",
        "type": "STRING"
    },
    {
        "name": "campaignName",
        "type": "STRING"
    },
    {
        "name": "formName",
        "type": "STRING"
    },
    {
        "name": "jobRole",
        "type": "STRING"
    },
    {
        "name": "leadTypeSalesOrMarketing",
        "type": "STRING"
    },
    {
        "name": "marketingPermission",
        "type": "STRING"
    },
    {
        "name": "marketingPermissionConfirmedByEmail",
        "type": "STRING"
    },
    {
        "name": "country",
        "type": "STRING"
    },
    {
        "name": "company",
        "type": "STRING"
    },
    {
        "name": "persona",
        "type": "STRING"
    },
    {
        "name": "utmCampaign",
        "type": "STRING"
    },
    {
        "name": "utmSource",
        "type": "STRING"
    },
    {
        "name": "utmMedium",
        "type": "STRING"
    },
    {
        "name": "dataCardExternalId",
        "type": "STRING"
    },
    {
        "name": "dataCardCreatedAt",
        "type": "DATETIME"
    },
    {
        "name": "dataCardUpdatedAt",
        "type": "DATETIME"
    }
]