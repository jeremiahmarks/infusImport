permissionsTable={
 }
ActionSequence = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "TemplateName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "VisibleToTheseUsers": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  } 
}
AffResource = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Notes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ProgramIds": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ResourceHREF": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ResourceHTML": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ResourceOrder": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ResourceType": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Title": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
Affiliate = {
  "AffCode": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "AffName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "DefCommissionType": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LeadAmt": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LeadCookieFor": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LeadPercent": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "NotifyLead": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "NotifySale": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ParentId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Password": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PayoutType": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "SaleAmt": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "SalePercent": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Status": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, }
CCharge = {
  "Amt": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "ApprCode": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "CCId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "MerchantId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "OrderNum": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "PaymentId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "RefNum": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
CProgram = {
  "Active": {
      "type": "Boolean", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillingType": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "DefaultCycle": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "DefaultFrequency": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "DefaultPrice": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Description": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Family": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "HideInStore": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LargeImage": {
      "type": "Blob", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProgramName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShortDescription": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Sku": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Status": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Taxable": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
Campaign = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Status": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
CampaignStep = {
  "CampaignId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "StepStatus": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StepTitle": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "TemplateId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
Campaignee = {
  "Campaign": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "CampaignId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Status": {
      "type": "Enum", 
      'permissions' : [ "Read", ] 
  }
} 
Company = {
  "AccountId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address1Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address2Street1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address2Street2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address2Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address3Street1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address3Street2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address3Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Anniversary": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "AssistantName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "AssistantPhone": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "BillingInformation": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Birthday": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "City": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "City2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "City3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Company": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CompanyID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactNotes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactType": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Country": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Country2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Country3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CreatedBy": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Email": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "EmailAddress2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "EmailAddress3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax1Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax2Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "FirstName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Groups": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "JobTitle": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LastName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LastUpdated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "LastUpdatedBy": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "MiddleName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Nickname": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "OwnerID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Password": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone1Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone1Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone2Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone2Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone3Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone3Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone4": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone4Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone4Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone5": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone5Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone5Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PostalCode": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PostalCode2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PostalCode3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ReferralCode": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "SpouseName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "State": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "State2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "State3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "StreetAddress1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "StreetAddress2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Suffix": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Title": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Username": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Validated": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Website": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ZipFour1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ZipFour2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ZipFour3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
Contact = {
  "AccountId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address1Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address2Street1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address2Street2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address2Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address3Street1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address3Street2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Address3Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Anniversary": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "AssistantName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "AssistantPhone": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "BillingInformation": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Birthday": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "City": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "City2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "City3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Company": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CompanyID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactNotes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactType": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Country": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Country2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Country3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CreatedBy": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Email": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "EmailAddress2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "EmailAddress3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax1Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Fax2Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "FirstName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Groups": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "JobTitle": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LastName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LastUpdated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "LastUpdatedBy": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LeadSourceId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Leadsource": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "MiddleName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Nickname": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "OwnerID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Password": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone1Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone1Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone2Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone2Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone3Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone3Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone4": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone4Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone4Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone5": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone5Ext": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Phone5Type": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PostalCode": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PostalCode2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PostalCode3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ReferralCode": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "SpouseName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "State": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "State2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "State3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "StreetAddress1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "StreetAddress2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Suffix": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Title": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Username": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Validated": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Website": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ZipFour1": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ZipFour2": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ZipFour3": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
ContactAction = {
  "Accepted": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ActionDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ActionDescription": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ActionType": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CompletionDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CreatedBy": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CreationDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CreationNotes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "EndDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "IsAppointment": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LastUpdated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "LastUpdatedBy": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ObjectType": {
      "type": "Enum", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "OpportunityId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PopupDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Priority": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "UserID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
ContactGroup = {
  "GroupCategoryId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "GroupDescription": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "GroupName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
ContactGroupAssign = {
  "Contact.Address1Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Address2Street1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Address2Street2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Address2Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Address3Street1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Address3Street2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Address3Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Anniversary": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.AssistantName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.AssistantPhone": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.BillingInformation": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Birthday": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.City": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.City2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.City3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Company": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.CompanyID": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.ContactNotes": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.ContactType": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Country": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Country2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Country3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.CreatedBy": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Email": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.EmailAddress2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.EmailAddress3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Fax1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Fax1Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Fax2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Fax2Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.FirstName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Groups": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.JobTitle": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.LastName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.LastUpdated": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.LastUpdatedBy": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Leadsource": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.MiddleName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Nickname": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.OwnerID": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone1Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone1Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone2Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone2Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone3Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone3Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone4": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone4Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone4Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone5": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone5Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Phone5Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.PostalCode": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.PostalCode2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.PostalCode3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.ReferralCode": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.SpouseName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.State": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.State2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.State3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.StreetAddress1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.StreetAddress2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Suffix": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Title": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.Website": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.ZipFour1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.ZipFour2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Contact.ZipFour3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "ContactGroup": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "GroupId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
ContactGroupCategory = {
  "CategoryDescription": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "CategoryName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
CreditCard = {
  "BillAddress1": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillAddress2": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillCity": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillCountry": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillState": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillZip": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "CVV2": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", ] 
  }, 
  "CardNumber": {
      "type": "String", 
      'permissions' : [ "Add", ] 
  }, 
  "CardType": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "Email": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ExpirationMonth": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ExpirationYear": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "FirstName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Last4": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "LastName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "MaestroIssueNumber": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "NameOnCard": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "PhoneNumber": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipAddress1": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipAddress2": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipCity": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipCompanyName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipCountry": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipFirstName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipLastName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipMiddleName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipPhoneNumber": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipState": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipZip": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "StartDateMonth": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "StartDateYear": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Status": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }
} 
DataFormField = {
  "DataType": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "DefaultValue": {
      "type": "String", 
      'permissions' : [ "Edit", "Read", ] 
  }, 
  "FormId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "GroupId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Label": {
      "type": "String", 
      'permissions' : [ "Edit", "Read", ] 
  }, 
  "ListRows": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Edit", "Read", ] 
  }, 
  "Values": {
      "type": "String", 
      'permissions' : [ "Edit", "Read", ] 
  }
} 
DataFormGroup = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "TabId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
DataFormTab = {
  "FormId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "TabName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
Expense = {
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "DateIncurred": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "ExpenseAmt": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "ExpenseType": {
      "type": "Enum", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "TypeId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
FileBox = {
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Extension": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "FileName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "FileSize": {
      "type": "Long", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Public": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }
} 
GroupAssign = {
  "Admin": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "GroupId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "UserId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
Invoice = {
  "AffiliateId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "CreditStatus": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Description": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "InvoiceTotal": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "InvoiceType": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "JobId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LeadAffiliateId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PayPlanStatus": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "PayStatus": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "ProductSold": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "PromoCode": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "RefundStatus": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "Synced": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "TotalDue": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "TotalPaid": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }
} 
InvoiceItem = {
  "CommissionStatus": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Description": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Discount": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "InvoiceAmt": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "InvoiceId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "OrderItemId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
InvoicePayment = {
  "Amt": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "InvoiceId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PayDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "PayStatus": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "PaymentId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "SkipCommission": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }
} 
Job = {
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DueDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "JobNotes": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "JobRecurringId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "JobStatus": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "JobTitle": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "OrderStatus": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "OrderType": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipCity": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipCompany": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipCountry": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipFirstName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipLastName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipMiddleName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipPhone": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipState": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipStreet1": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipStreet2": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShipZip": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "StartDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
JobRecurringInstance = {
  "AutoCharge": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Description": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "EndDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "InvoiceItemId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "RecurringId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "StartDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Status": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
Lead = {
  "AffiliateId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CreatedBy": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Read", ] 
  }, 
  "EstimatedCloseDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LastUpdated": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Read", ] 
  }, 
  "LastUpdatedBy": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Leadsource": {
      "type": "String", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "NextActionDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "NextActionNotes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Objection": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "OpportunityNotes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "OpportunityTitle": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ProjectedRevenueHigh": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ProjectedRevenueLow": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "StageID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "StatusID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "UserID": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
LeadSource = {
  "CostPerLead": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Description": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "EndDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LeadSourceCategoryId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Medium": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Message": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "StartDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Status": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Vendor": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
LeadSourceCategory = {
  "Description": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
LeadSourceExpense = {
  "Amount": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "DateIncurred": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LeadSourceId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LeadSourceRecurringExpenseId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Notes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Title": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
LeadSourceRecurringExpense = {
  "Amount": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "EndDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LeadSourceId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "NextExpenseDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Notes": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "StartDate": {
      "type": "DateTime", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Title": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
MtgLead = {
  "ActualCloseDate": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "ApplicationDate": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "CreditReportDate": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateAppraisalDone": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateAppraisalOrdered": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateAppraisalReceived": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateRateLockExpires": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateRateLocked": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateTitleOrdered": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateTitleReceived": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "FundingDate": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
OrderItem = {
  "CPU": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ItemDescription": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ItemName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ItemType": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Notes": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "OrderId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "PPU": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Qty": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "SubscriptionPlanId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
PayPlan = {
  "AmtDue": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "DateDue": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "FirstPayAmt": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "InitDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "InvoiceId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "StartDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "Type": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }
} 
PayPlanItem = {
  "AmtDue": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "AmtPaid": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "DateDue": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PayPlanId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Status": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }
} 
Payment = {
  "ChargeId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Commission": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "InvoiceId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PayAmt": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "PayDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "PayNote": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "PayType": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "RefundId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Synced": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "UserId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
Product = {
  "BottomHTML": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "CityTaxable": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "CountryTaxable": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Description": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "HideInStore": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "InventoryLimit": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "InventoryNotifiee": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "IsPackage": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "LargeImage": {
      "type": "Blob", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "NeedsDigitalDelivery": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductPrice": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Shippable": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShippingTime": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShortDescription": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Sku": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "StateTaxable": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Status": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Taxable": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "TopHTML": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Weight": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
ProductCategory = {
  "CategoryDisplayName": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CategoryImage": {
      "type": "Blob", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CategoryOrder": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ParentId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
ProductCategoryAssign = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ProductCategoryId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
ProductInterest = {
  "DiscountPercent": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ObjType": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ObjectId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ProductType": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Qty": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
ProductInterestBundle = {
  "BundleName": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Description": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
ProductOptValue = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "IsDefault": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Label": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "OptionIndex": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "PriceAdjustment": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ProductOptionId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Sku": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
ProductOption = {
  "AllowSpaces": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CanContain": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CanEndWith": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CanStartWith": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "IsRequired": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Label": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "MaxChars": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "MinChars": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "OptionType": {
      "type": "Enum", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Order": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "TextMessage": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
RecurringOrder = {
  "AffiliateId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "AutoCharge": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillingAmt": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "BillingCycle": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "CC1": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "CC2": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "EndDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Frequency": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LastBillDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "LeadAffiliateId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "MaxRetry": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "MerchantAccountId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "NextBillDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "NumDaysBetweenRetry": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "OriginatingOrderId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PaidThruDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProgramId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "PromoCode": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Qty": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ReasonStopped": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ShippingOptionId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "StartDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Status": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "SubscriptionPlanId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
RecurringOrderWithContact = {
  "AffiliateId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "AutoCharge": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "BillingAmt": {
      "type": "Double", 
      'permissions' : [ "Read", ] 
  }, 
  "BillingCycle": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "CC1": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "CC2": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "City": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Country": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Email": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "EmailAddress2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "EmailAddress3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "EndDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "FirstName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Frequency": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "LastBillDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "LastName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "LeadAffiliateId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "MaxRetry": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "MerchantAccountId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "MiddleName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "NextBillDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "Nickname": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "NumDaysBetweenRetry": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "PaidThruDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone1Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone1Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone2Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone2Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "PostalCode": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ProgramId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PromoCode": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Qty": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "ReasonStopped": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "RecurringOrderId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ShippingOptionId": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "SpouseName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StartDate": {
      "type": "Date", 
      'permissions' : [ "Read", ] 
  }, 
  "State": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Status": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StreetAddress1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StreetAddress2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "SubscriptionPlanId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Suffix": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Title": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "ZipFour1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
Referral = {
  "AffiliateId": {
      "type": "Id", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "DateExpires": {
      "type": "Date", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "DateSet": {
      "type": "Date", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "IPAddress": {
      "type": "String", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Info": {
      "type": "String", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "Source": {
      "type": "String", 
      'permissions' : [ "Add", "Read", ] 
  }, 
  "Type": {
      "type": "Integer", 
      'permissions' : [ "Add", "Read", ] 
  }
} 
SavedFilter = {
  "FilterName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "ReportStoredName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "UserId": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
Stage = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "StageName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StageOrder": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }, 
  "TargetNumDays": {
      "type": "Integer", 
      'permissions' : [ "Read", ] 
  }
} 
StageMove = {
  "CreatedBy": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "MoveDate": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "MoveFromStage": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "MoveToStage": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "OpportunityId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PrevStageMoveDate": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "UserId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }
} 
Status = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "StatusName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StatusOrder": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "TargetNumDays": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
SubscriptionPlan = {
  "Active": {
      "type": "Boolean", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Cycle": {
      "type": "String", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Frequency": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PlanPrice": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "PreAuthorizeAmount": {
      "type": "Double", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "ProductId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }, 
  "Prorate": {
      "type": "Boolean", 
      'permissions' : [ "Edit", "Add", "Read", ] 
  }
} 
Template = {
  "Categories": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "PieceTitle": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "PieceType": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
Ticket = {
  "CloseDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "ContactId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "CreatedBy": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "DateCreated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "DateInStage": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "DevId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "FolowUpDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "HasCustomerCalled": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "IssueId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "LastUpdated": {
      "type": "DateTime", 
      'permissions' : [ "Read", ] 
  }, 
  "LastUpdatedBy": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Ordering": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Priority": {
      "type": "Integer", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Stage": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "Summary": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "TargetCompletionDate": {
      "type": "Date", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "TicketApplication": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "TicketCategory": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "TicketTitle": {
      "type": "String", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "TicketTypeId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "TimeSpent": {
      "type": "Double", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }, 
  "UserId": {
      "type": "Id", 
      'permissions' : [ "Edit", "Delete", "Add", "Read", ] 
  }
} 
TicketStage = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "StageName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
TicketType = {
  "CategoryId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Label": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
User = {
  "City": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Email": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "EmailAddress2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "EmailAddress3": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "FirstName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "LastName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "MiddleName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Nickname": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone1Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone1Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone2Ext": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Phone2Type": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "PostalCode": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "SpouseName": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "State": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StreetAddress1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "StreetAddress2": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Suffix": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "Title": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "ZipFour1": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }
} 
UserGroup = {
  "Id": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
  "Name": {
      "type": "String", 
      'permissions' : [ "Read", ] 
  }, 
  "OwnerId": {
      "type": "Id", 
      'permissions' : [ "Read", ] 
  }, 
}
permissionsTable["ActionSequence"] = ActionSequence
permissionsTable["AffResource"] = AffResource
permissionsTable["Affiliate"] = Affiliate
permissionsTable["CCharge"] = CCharge
permissionsTable["CProgram"] = CProgram
permissionsTable["Campaign"] = Campaign
permissionsTable["CampaignStep"] = CampaignStep
permissionsTable["Campaignee"] = Campaignee
permissionsTable["Company"] = Company
permissionsTable["Contact"] = Contact
permissionsTable["ContactAction"] = ContactAction
permissionsTable["ContactGroup"] = ContactGroup
permissionsTable["ContactGroupAssign"] = ContactGroupAssign
permissionsTable["ContactGroupCategory"] = ContactGroupCategory
permissionsTable["CreditCard"] = CreditCard
permissionsTable["DataFormField"] = DataFormField
permissionsTable["DataFormGroup"] = DataFormGroup
permissionsTable["DataFormTab"] = DataFormTab
permissionsTable["Expense"] = Expense
permissionsTable["FileBox"] = FileBox
permissionsTable["GroupAssign"] = GroupAssign
permissionsTable["Invoice"] = Invoice
permissionsTable["InvoiceItem"] = InvoiceItem
permissionsTable["InvoicePayment"] = InvoicePayment
permissionsTable["Job"] = Job
permissionsTable["JobRecurringInstance"] = JobRecurringInstance
permissionsTable["Lead"] = Lead
permissionsTable["LeadSource"] = LeadSource
permissionsTable["LeadSourceCategory"] = LeadSourceCategory
permissionsTable["LeadSourceExpense"] = LeadSourceExpense
permissionsTable["LeadSourceRecurringExpense"] = LeadSourceRecurringExpense
permissionsTable["MtgLead"] = MtgLead
permissionsTable["OrderItem"] = OrderItem
permissionsTable["PayPlan"] = PayPlan
permissionsTable["PayPlanItem"] = PayPlanItem
permissionsTable["Payment"] = Payment
permissionsTable["Product"] = Product
permissionsTable["ProductCategory"] = ProductCategory
permissionsTable["ProductCategoryAssign"] = ProductCategoryAssign
permissionsTable["ProductInterest"] = ProductInterest
permissionsTable["ProductInterestBundle"] = ProductInterestBundle
permissionsTable["ProductOptValue"] = ProductOptValue
permissionsTable["ProductOption"] = ProductOption
permissionsTable["RecurringOrder"] = RecurringOrder
permissionsTable["RecurringOrderWithContact"] = RecurringOrderWithContact
permissionsTable["Referral"] = Referral
permissionsTable["SavedFilter"] = SavedFilter
permissionsTable["Stage"] = Stage
permissionsTable["StageMove"] = StageMove
permissionsTable["Status"] = Status
permissionsTable["SubscriptionPlan"] = SubscriptionPlan
permissionsTable["Template"] = Template
permissionsTable["Ticket"] = Ticket
permissionsTable["TicketStage"] = TicketStage
permissionsTable["TicketType"] = TicketType
permissionsTable["User"] = User
permissionsTable["UserGroup"] = UserGroup