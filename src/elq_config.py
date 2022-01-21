activity_export_def = {
    "EmailOpen": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "EmailSendType": "{{Activity.Field(EmailSendType)}}"
    },
    "EmailClickthrough": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "EmailSendType": "{{Activity.Field(EmailSendType)}}"
    },
    "EmailSend": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "EmailSendType": "{{Activity.Field(EmailSendType)}}"
    },
    "FormSubmit": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "Subscribe": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "Unsubscribe": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}"
    },
    "WebVisit": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "Duration": "{{Activity.Field(Duration)}}",
        "NumberOfPages": "{{Activity.Field(NumberOfPages)}}",
        "ReferrerUrl": "{{Activity.Field(ReferrerUrl)}}",
        "FirstPageViewUrl": "{{Activity.Field(FirstPageViewUrl)}}"
    },
    "PageView": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "VisitorId": "{{Activity.Visitor.Id}}",
        "VisitorExternalId": "{{Activity.Visitor.ExternalId}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "ReferrerUrl": "{{Activity.Field(ReferrerUrl)}}",
        "Url": "{{Activity.Field(Url)}}",
        "WebVisitId": "{{Activity.Field(WebVisitId)}}"

    },
    "Bounceback": {
        "ActivityId": "{{Activity.Id}}",
        "ContactId": "{{Activity.Contact.Id}}",
        "ActivityType": "{{Activity.Type}}",
        "ActivityDate": "{{Activity.CreatedAt}}",
        "AssetType": "{{Activity.Asset.Type}}",
        "AssetName": "{{Activity.Asset.Name}}",
        "AssetId": "{{Activity.Asset.Id}}",
        "CampaignId": "{{Activity.Campaign.Id}}",
        "ExternalId": "{{Activity.ExternalId}}",
        "SmtpErrorCode": "{{Activity.Field(SmtpErrorCode)}}",
        "SmtpStatusCode": "{{Activity.Field(SmtpStatusCode)}}",
        "SmtpMessage": "{{Activity.Field(SmtpMessage)}}"
    }
}

contact_export_def = {
    "ContactID": "{{Contact.Id}}",
    "Company": "{{Contact.Field(C_Company)}}",
    "City": "{{Contact.Field(C_City)}}",
    "Country": "{{Contact.Field(C_Country)}}",
    "Title": "{{Contact.Field(C_Title)}}",
    "CreatedAt": "{{Contact.Field(C_DateCreated)}}",
    "UpdatedAt": "{{Contact.Field(C_DateModified)}}",
    "Industry": "{{Contact.Field(C_Industry1)}}",
    "AnnualRevenue": "{{Contact.Field(C_Annual_Revenue1)}}",
    "EmailDomain": "{{Contact.Field(C_EmailAddressDomain)}}",
    "MarketingPermission": "{{Contact.Field(C_Marketing_permission1)}}",
    "MarketingPermissionDate": "{{Contact.Field(C_Marketing_permission_date1)}}"
}

contact_time_series_export_def = {
    "ContactID": "{{Contact.Id}}",
    "Company": "{{Contact.Field(C_Company)}}",
    "City": "{{Contact.Field(C_City)}}",
    "Country": "{{Contact.Field(C_Country)}}",
    "Title": "{{Contact.Field(C_Title)}}",
    "CreatedAt": "{{Contact.Field(C_DateCreated)}}",
    "UpdatedAt": "{{Contact.Field(C_DateModified)}}",
    "Industry": "{{Contact.Field(C_Industry1)}}",
    "AnnualRevenue": "{{Contact.Field(C_Annual_Revenue1)}}",
    "EmailDomain": "{{Contact.Field(C_EmailAddressDomain)}}",
    "MarketingPermission": "{{Contact.Field(C_Marketing_permission1)}}",
    "MarketingPermissionDate": "{{Contact.Field(C_Marketing_permission_date1)}}",
    "LeadRating": "{{Contact.Field(C_Lead_Rating___Combined1)}}"
}

account_export_def = {
    "CompanyID": "{{Account.Field(CompanyIDExt)}}",
    "Company": "{{Account.Field(M_CompanyName)}}",
    "Country": "{{Account.Field(M_Country)}}",
    "Address": "{{Account.Field(M_Address1)}}",
    "City": "{{Account.Field(M_City)}}",
    "StateOrProvince": "{{Account.Field(M_State_Prov)}}",
    "ZipCode": "{{Account.Field(M_Zip_Postal)}}",
    "BusinessPhone": "{{Account.Field(M_BusPhone)}}",
    "CreatedAt": "{{Account.Field(M_DateCreated)}}",
    "UpdatedAt": "{{Account.Field(M_DateModified)}}"
}

cdo_id = "6"

cdo_export_def = {
    "id": "{{CustomObject[6].Contact.Id}}",
    "formName": "{{CustomObject[6].Field[142]}}",
    "leadTypeSalesOrMarketing": "{{CustomObject[6].Field[145]}}",
    "marketingPermission": "{{CustomObject[6].Field[146]}}",
    "campaignName": "{{CustomObject[6].Field[147]}}",
    "country": "{{CustomObject[6].Field[150]}}",
    "company": "{{CustomObject[6].Field[151]}}",
    "utmCampaign": "{{CustomObject[6].Field[152]}}",
    "utmSource": "{{CustomObject[6].Field[153]}}",
    "utmMedium": "{{CustomObject[6].Field[154]}}",
    "jobRole": "{{CustomObject[6].Field[158]}}",
    "persona": "{{CustomObject[6].Field[159]}}",
    "marketingPermissionConfirmedByEmail": "{{CustomObject[6].Field[160]}}",
    "campaignType": "{{CustomObject[6].Field[161]}}",
    "dataCardExternalId": "{{CustomObject[6].ExternalId}}",
    "dataCardCreatedAt": "{{CustomObject[6].CreatedAt}}",
    "dataCardUpdatedAt": "{{CustomObject[6].UpdatedAt}}"
}