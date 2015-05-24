import sqlite3
projectDevServer="home/jlmarks/infusImport/ISServer/csvDatabase/DEV.sqlite"
# engine=create_engine(projectDevServer)
# cursor.execute('''
#     CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
#                        phone TEXT, email TEXT unique, password TEXT)
# ''')
db=sqlite3.connect("/home/jlmarks/infusImport/ISServer/csvDatabase/DEV.sqlite")
cursor=db.cursor()

tableCreators=[]
tablenames=[
    "Actionsequence",
    "Affresource",
    "Affiliate",
    "Ccharge",
    "Cprogram",
    "Campaign",
    "Campaignstep",
    "Campaignee",
    "Company",
    "Contact",
    "Contactaction",
    "Contactgroup",
    "ContactgroupAssign",
    "ContactgroupCategory",
    "Creditcard",
    "DataformField",
    "DataformGroup",
    "DataformTab",
    "Expense",
    "Filebox",
    "Groupassign",
    "Invoice",
    "Invoiceitem",
    "Invoicepayment",
    "Job",
    "JobrecurringInstance",
    "Lead",
    "Leadsource",
    "LeadsourceCategory",
    "LeadsourceExpense",
    "LeadsourceRecurringExpense",
    "Mtglead",
    "Orderitem",
    "Payplan",
    "PayplanItem",
    "Payment",
    "Product",
    "Productcategory",
    "ProductcategoryAssign",
    "Productinterest",
    "ProductinterestBundle",
    "ProductoptValue",
    "Productoption",
    "Recurringorder",
    "RecurringorderWithContact",
    "Referral",
    "Savedfilter",
    "Stage",
    "Stagemove",
    "Status",
    "Subscriptionplan",
    "Template",
    "Ticket",
    "Ticketstage",
    "Tickettype",
    "User",
    "Usergroup",
    ]

for eachTable in tablenames:
    cursor.execute("DROP TABLE IF EXISTS "+ eachTable)
    print eachTable + "Dropped"

tableCreators.append("""CREATE TABLE Actionsequence(
        Id Integer, primary_key,
        TemplateName String(250),
        VisibleToTheseUsers String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Affresource(
        Id Integer, primary_key,
        Notes String(250),
        ProgramIds String(250),
        ResourceHREF String(250),
        ResourceHTML String(250),
        ResourceOrderf String(250),
        ResourceType String(250),
        Title String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Affiliate(
        AffCode String(250),
        AffName String(250),
        ContactId Integer, ForeignKey'Contact.Id',
        DefCommissionType Integer,
        Id Integer, primary_key,
        LeadAmt Float,
        LeadCookieFor Integer,
        LeadPercent Float,
        NotifyLead Integer,
        NotifySale Integer,
        ParentId Integer,
        Password String(250),
        PayoutType Integer,
        SaleAmt Float,
        SalePercent Float,
        Status Integer
    )
    """)
tableCreators.append("""CREATE TABLE Ccharge(
        Amt Float,
        ApprCode String(250),
        CCId Integer ForeignKey'Creditcard.Id',
        Id Integer, primary_key,
        MerchantId Id,
        OrderNum String(250),
        PaymentId Id,
        RefNum String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Cprogram(
        Active Boolean,
        BillingType String(250),
        DefaultCycle String(250),
        DefaultFrequency Integer,
        DefaultPrice Float,
        Description String(250),
        Family String(250),
        HideInStore Integer,
        Id Integer, primary_key,
        LargeImage Blob,
        ProductId Id,
        ProgramName String(250),
        ShortDescription String(250),
        Sku String(250),
        Status Integer,
        Taxable Integer
    )
    """)
tableCreators.append("""CREATE TABLE Campaign(
        Id Integer, primary_key,
        Name String(250),
        Status String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Campaignstep(
        CampaignId Id,
        Id Integer, primary_key,
        StepStatus String(250),
        StepTitle String(250),
        TemplateId Id
    )
    """)

tableCreators.append("""CREATE TABLE Campaignee(
        Campaign String(250),
        CampaignId Id,
        ContactId Id,
        Status Integer
    )
    """)

tableCreators.append("""CREATE TABLE Company(
        AccountId Id,
        Address1Type String(250),
        Address2Street1 String(250),
        Address2Street2 String(250),
        Address2Type String(250),
        Address3Street1 String(250),
        Address3Street2 String(250),
        Address3Type String(250),
        Anniversary Date,
        AssistantName String(250),
        AssistantPhone String(250),
        BillingInformation String(250),
        Birthday Date,
        City String(250),
        City2 String(250),
        City3 String(250),
        Company String(250),
        CompanyID Id,
        ContactNotes String(250),
        ContactType String(250),
        Country String(250),
        Country2 String(250),
        Country3 String(250),
        CreatedBy Id,
        DateCreated DateTime,
        Email String(250),
        EmailAddress2 String(250),
        EmailAddress3 String(250),
        Fax1 String(250),
        Fax1Type String(250),
        Fax2 String(250),
        Fax2Type String(250),
        FirstName String(250),
        Groups String(250),
        Id Integer, primary_key,
        JobTitle String(250),
        LastName String(250),
        LastUpdated DateTime,
        LastUpdatedBy Id,
        MiddleName String(250),
        Nickname String(250),
        OwnerID Id,
        Password String(250),
        Phone1 String(250),
        Phone1Ext String(250),
        Phone1Type String(250),
        Phone2 String(250),
        Phone2Ext String(250),
        Phone2Type String(250),
        Phone3 String(250),
        Phone3Ext String(250),
        Phone3Type String(250),
        Phone4 String(250),
        Phone4Ext String(250),
        Phone4Type String(250),
        Phone5 String(250),
        Phone5Ext String(250),
        Phone5Type String(250),
        PostalCode String(250),
        PostalCode2 String(250),
        PostalCode3 String(250),
        ReferralCode String(250),
        SpouseName String(250),
        State String(250),
        State2 String(250),
        State3 String(250),
        StreetAddress1 String(250),
        StreetAddress2 String(250),
        Suffix String(250),
        Title String(250),
        Username String(250),
        Validated String(250),
        Website String(250),
        ZipFour1 String(250),
        ZipFour2 String(250),
        ZipFour3 String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Contact(
        AccountId Id,
        Address1Type String(250),
        Address2Street1 String(250),
        Address2Street2 String(250),
        Address2Type String(250),
        Address3Street1 String(250),
        Address3Street2 String(250),
        Address3Type String(250),
        Anniversary Date,
        AssistantName String(250),
        AssistantPhone String(250),
        BillingInformation String(250),
        Birthday Date,
        City String(250),
        City2 String(250),
        City3 String(250),
        Company String(250),
        CompanyID Id,
        ContactNotes String(250),
        ContactType String(250),
        Country String(250),
        Country2 String(250),
        Country3 String(250),
        CreatedBy Id,
        DateCreated DateTime,
        Email String(250),
        EmailAddress2 String(250),
        EmailAddress3 String(250),
        Fax1 String(250),
        Fax1Type String(250),
        Fax2 String(250),
        Fax2Type String(250),
        FirstName String(250),
        Groups String(250),
        Id Integer, primary_key,
        JobTitle String(250),
        LastName String(250),
        LastUpdated DateTime,
        LastUpdatedBy Id,
        LeadSourceId Id,
        Leadsource String(250),
        MiddleName String(250),
        Nickname String(250),
        OwnerID Id,
        Password String(250),
        Phone1 String(250),
        Phone1Ext String(250),
        Phone1Type String(250),
        Phone2 String(250),
        Phone2Ext String(250),
        Phone2Type String(250),
        Phone3 String(250),
        Phone3Ext String(250),
        Phone3Type String(250),
        Phone4 String(250),
        Phone4Ext String(250),
        Phone4Type String(250),
        Phone5 String(250),
        Phone5Ext String(250),
        Phone5Type String(250),
        PostalCode String(250),
        PostalCode2 String(250),
        PostalCode3 String(250),
        ReferralCode String(250),
        SpouseName String(250),
        State String(250),
        State2 String(250),
        State3 String(250),
        StreetAddress1 String(250),
        StreetAddress2 String(250),
        Suffix String(250),
        Title String(250),
        Username String(250),
        Validated String(250),
        Website String(250),
        ZipFour1 String(250),
        ZipFour2 String(250),
        ZipFour3 String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Contactaction(
        Accepted Integer,
        ActionDate DateTime,
        ActionDescription String(250),
        ActionType String(250),
        CompletionDate DateTime,
        ContactId Id,
        CreatedBy Id,
        CreationDate DateTime,
        CreationNotes String(250),
        EndDate DateTime,
        Id Integer, primary_key,
        IsAppointment Integer,
        LastUpdated DateTime,
        LastUpdatedBy Id,
        ObjectType Integer,
        OpportunityId Id,
        PopupDate DateTime,
        Priority Integer,
        UserID Id
    )
    """)

tableCreators.append("""CREATE TABLE Contactgroup(
        GroupCategoryId Id,
        GroupDescription String(250),
        GroupName String(250),
        Id Integer, primary_key
    )
    """)

tableCreators.append("""CREATE TABLE ContactgroupAssign(
        Contact_Address1Type,
        Contact_Address2Street1,
        Contact_Address2Street2,
        Contact_Address2Type,
        Contact_Address3Street1,
        Contact_Address3Street2,
        Contact_Address3Type,
        Contact_Anniversary,
        Contact_AssistantName,
        Contact_AssistantPhone,
        Contact_BillingInformation String,
        Contact_Birthday,
        Contact_City,
        Contact_City2,
        Contact_City3,
        Contact_Company,
        Contact_CompanyID,
        Contact_ContactNotes,
        Contact_ContactType,
        Contact_Country,
        Contact_Country2,
        Contact_Country3,
        Contact_CreatedBy,
        Contact_DateCreated,
        Contact_Email,
        Contact_EmailAddress2,
        Contact_EmailAddress3,
        Contact_Fax1,
        Contact_Fax1Type,
        Contact_Fax2,
        Contact_Fax2Type,
        Contact_FirstName,
        Contact_Groups,
        Contact_Id,
        Contact_JobTitle,
        Contact_LastName,
        Contact_LastUpdated,
        Contact_LastUpdatedBy,
        Contact_Leadsource,
        Contact_MiddleName,
        Contact_Nickname,
        Contact_OwnerID,
        Contact_Phone1,
        Contact_Phone1Ext,
        Contact_Phone1Type,
        Contact_Phone2,
        Contact_Phone2Ext,
        Contact_Phone2Type,
        Contact_Phone3,
        Contact_Phone3Ext,
        Contact_Phone3Type,
        Contact_Phone4,
        Contact_Phone4Ext,
        Contact_Phone4Type,
        Contact_Phone5,
        Contact_Phone5Ext,
        Contact_Phone5Type,
        Contact_PostalCode,
        Contact_PostalCode2,
        Contact_PostalCode3,
        Contact_ReferralCode,
        Contact_SpouseName,
        Contact_State,
        Contact_State2,
        Contact_State3,
        Contact_StreetAddress1,
        Contact_StreetAddress2,
        Contact_Suffix,
        Contact_Title,
        Contact_Website,
        Contact_ZipFour1,
        Contact_ZipFour2,
        Contact_ZipFour3,
        ContactGroup String(250),
        ContactId Id,
        DateCreated DateTime,
        GroupId Id
    )
    """)

tableCreators.append("""CREATE TABLE ContactgroupCategory(
        CategoryDescription String(250),
        CategoryName String(250),
        Id Integer, primary_key
    )
    """)

tableCreators.append("""CREATE TABLE Creditcard(
        BillAddress1 String(250),
        BillAddress2 String(250),
        BillCity String(250),
        BillCountry String(250),
        BillName String(250),
        BillState String(250),
        BillZip String(250),
        CVV2 String(250),
        CardNumber String(250),
        CardType String(250),
        ContactId Id,
        Email String(250),
        ExpirationMonth String(250),
        ExpirationYear String(250),
        FirstName String(250),
        Id Integer, primary_key,
        Last4 String(250),
        LastName String(250),
        MaestroIssueNumber String(250),
        NameOnCard String(250),
        PhoneNumber String(250),
        ShipAddress1 String(250),
        ShipAddress2 String(250),
        ShipCity String(250),
        ShipCompanyName String(250),
        ShipCountry String(250),
        ShipFirstName String(250),
        ShipLastName String(250),
        ShipMiddleName String(250),
        ShipName String(250),
        ShipPhoneNumber String(250),
        ShipState String(250),
        ShipZip String(250),
        StartDateMonth String(250),
        StartDateYear String(250),
        Status Integer
    )
    """)

tableCreators.append("""CREATE TABLE DataformField(
        DataType Integer,
        DefaultValue String(250),
        FormId Id,
        GroupId Id,
        Id Integer, primary_key,
        Label String(250),
        ListRows Integer,
        Name String(250),
        ValuesF String(250)
    )
    """)

tableCreators.append("""CREATE TABLE DataformGroup(
        Id Integer, primary_key,
        Name String(250),
        TabId Id
    )
    """)

tableCreators.append("""CREATE TABLE DataformTab(
        FormId Id,
        Id Integer, primary_key,
        TabName String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Expense(
        ContactId Id,
        DateIncurred DateTime,
        ExpenseAmt Float,
        ExpenseType Integer,
        Id Integer, primary_key,
        TypeId Id
    )
    """)

tableCreators.append("""CREATE TABLE Filebox(
        ContactId Id,
        Extension String(250),
        FileName String(250),
        FileSize Long,
        Id Integer, primary_key,
        Public Integer
    )
    """)

tableCreators.append("""CREATE TABLE Groupassign(
        Admin Id,
        GroupId Id,
        Id Integer, primary_key,
        UserId Id
    )
    """)

tableCreators.append("""CREATE TABLE Invoice(
        AffiliateId Id,
        ContactId Id,
        CreditStatus Integer,
        DateCreated DateTime,
        Description String(250),
        Id Integer, primary_key,
        InvoiceTotal Float,
        InvoiceType String(250),
        JobId Id,
        LeadAffiliateId Id,
        PayPlanStatus Integer,
        PayStatus Integer,
        ProductSold String(250),
        PromoCode String(250),
        RefundStatus Integer,
        Synced Integer,
        TotalDue Float,
        TotalPaid Float
    )
    """)

tableCreators.append("""CREATE TABLE Invoiceitem(
        CommissionStatus Integer,
        DateCreated DateTime,
        Description String(250),
        Discount Float,
        Id Integer, primary_key,
        InvoiceAmt Float,
        InvoiceId Id,
        OrderItemId Id
    )
    """)

tableCreators.append("""CREATE TABLE Invoicepayment(
        Amt Float,
        Id Integer, primary_key,
        InvoiceId Id,
        PayDate Date,
        PayStatus String(250),
        PaymentId Id,
        SkipCommission Integer
    )
    """)

tableCreators.append("""CREATE TABLE Job(
        ContactId Id,
        DateCreated DateTime,
        DueDate Date,
        Id Integer, primary_key,
        JobNotes String(250),
        JobRecurringId Id,
        JobStatus String(250),
        JobTitle String(250),
        OrderStatus Integer,
        OrderType String(250),
        ProductId Id,
        ShipCity String(250),
        ShipCompany String(250),
        ShipCountry String(250),
        ShipFirstName String(250),
        ShipLastName String(250),
        ShipMiddleName String(250),
        ShipPhone String(250),
        ShipState String(250),
        ShipStreet1 String(250),
        ShipStreet2 String(250),
        ShipZip String(250),
        StartDate Date
    )
    """)

tableCreators.append("""CREATE TABLE JobrecurringInstance(
        AutoCharge Integer,
        DateCreated DateTime,
        Description String(250),
        EndDate Date,
        Id Integer, primary_key,
        InvoiceItemId Id,
        RecurringId Id,
        StartDate Date,
        Status Integer
    )
    """)
tableCreators.append("""CREATE TABLE Lead(
        AffiliateId Id,
        ContactID Id,
        CreatedBy Id,
        DateCreated DateTime,
        EstimatedCloseDate DateTime,
        Id Integer, primary_key,
        LastUpdated DateTime,
        LastUpdatedBy Id,
        Leadsource String(250),
        NextActionDate DateTime,
        NextActionNotes String(250),
        Objection String(250),
        OpportunityNotes String(250),
        OpportunityTitle String(250),
        ProjectedRevenueHigh Float,
        ProjectedRevenueLow Float,
        StageID Id,
        StatusID Id,
        UserID Id
    )
    """)

tableCreators.append("""CREATE TABLE Leadsource(
        CostPerLead String(250),
        Description String(250),
        EndDate Date,
        Id Integer, primary_key,
        LeadSourceCategoryId Id,
        Medium String(250),
        Message String(250),
        Name String(250),
        StartDate Date,
        Status String(250),
        Vendor String(250)
    )
    """)

tableCreators.append("""CREATE TABLE LeadsourceCategory(
        Description String(250),
        Id Integer, primary_key,
        Name String(250)
    )
    """)

tableCreators.append("""CREATE TABLE LeadsourceExpense(
        Amount Float,
        DateIncurred DateTime,
        Id Integer, primary_key,
        LeadSourceId Id,
        LeadSourceRecurringExpenseId Id,
        Notes String(250),
        Title String(250)
    )
    """)

tableCreators.append("""CREATE TABLE LeadsourceRecurringExpense(
        Amount Float,
        EndDate DateTime,
        Id Integer, primary_key,
        LeadSourceId Id,
        NextExpenseDate DateTime,
        Notes String(250),
        StartDate DateTime,
        Title String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Mtglead(
        ActualCloseDate DateTime,
        ApplicationDate DateTime,
        CreditReportDate DateTime,
        DateAppraisalDone DateTime,
        DateAppraisalOrdered DateTime,
        DateAppraisalReceived DateTime,
        DateRateLockExpires DateTime,
        DateRateLocked DateTime,
        DateTitleOrdered DateTime,
        DateTitleReceived DateTime,
        FundingDate DateTime,
        Id Integer, primary_key
    )
    """)

tableCreators.append("""CREATE TABLE Orderitem(
        CPU Float,
        Id Integer, primary_key,
        ItemDescription String(250),
        ItemName String(250),
        ItemType Integer,
        Notes String(250),
        OrderId Id,
        PPU Float,
        ProductId Id,
        Qty Integer,
        SubscriptionPlanId Id
    )
    """)

tableCreators.append("""CREATE TABLE Payplan(
        AmtDue Float,
        DateDue Date,
        FirstPayAmt Float,
        Id Integer, primary_key,
        InitDate Date,
        InvoiceId Id,
        StartDate Date,
        Type Integer
    )
    """)

tableCreators.append("""CREATE TABLE PayplanItem(
        AmtDue Float,
        AmtPaid Float,
        DateDue Date,
        Id Integer, primary_key,
        PayPlanId Id,
        Status Integer
    )
    """)

tableCreators.append("""CREATE TABLE Payment(
        ChargeId Id,
        Commission Integer,
        ContactId Id,
        Id Integer, primary_key,
        InvoiceId Id,
        PayAmt Float,
        PayDate Date,
        PayNote String(250),
        PayType String(250),
        RefundId Id,
        Synced Integer,
        UserId Id
    )
    """)

tableCreators.append("""CREATE TABLE Product(
        BottomHTML String(250),
        CityTaxable Integer,
        CountryTaxable Integer,
        Description String(250),
        HideInStore Integer,
        Id Integer, primary_key,
        InventoryLimit Integer,
        InventoryNotifiee String(250),
        IsPackage Integer,
        LargeImage Blob,
        NeedsDigitalDelivery Integer,
        ProductName String(250),
        ProductPrice Float,
        Shippable Integer,
        ShippingTime String(250),
        ShortDescription String(250),
        Sku String(250),
        StateTaxable Integer,
        Status Integer,
        Taxable Integer,
        TopHTML String(250),
        Weight Float
    )
    """)
tableCreators.append("""CREATE TABLE Productcategory(
        CategoryDisplayName String(250),
        CategoryImage Blob,
        CategoryOrderf Integer,
        Id Integer, primary_key,
        ParentId Id
    )
    """)

tableCreators.append("""CREATE TABLE ProductcategoryAssign(
        Id Integer, primary_key,
        ProductCategoryId Id,
        ProductId Id
    )
    """)

tableCreators.append("""CREATE TABLE Productinterest(
        DiscountPercent Integer,
        Id Integer, primary_key,
        ObjType String(250),
        ObjectId Id,
        ProductId Id,
        ProductType String(250),
        Qty Integer
    )
    """)
tableCreators.append("""CREATE TABLE ProductinterestBundle(
        BundleName String(250),
        Description String(250),
        Id Integer, primary_key
    )
    """)

tableCreators.append("""CREATE TABLE ProductoptValue(
        Id Integer, primary_key,
        IsDefault Integer,
        Label String(250),
        Name String(250),
        OptionIndex Integer,
        PriceAdjustment Float,
        ProductOptionId Id,
        Sku String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Productoption(
        AllowSpaces Integer,
        CanContain String(250),
        CanEndWith Integer,
        CanStartWith String(250),
        Id Integer, primary_key,
        IsRequired Integer,
        Label String(250),
        MaxChars Integer,
        MinChars Integer,
        Name String(250),
        OptionType Integer,
        Orderf Integer,
        ProductId Id,
        TextMessage Integer
    )
    """)
tableCreators.append("""CREATE TABLE Recurringorder(
        AffiliateId Id,
        AutoCharge Integer,
        BillingAmt Float,
        BillingCycle String(250),
        CC1 Id,
        CC2 Id,
        ContactId Id,
        EndDate Date,
        Frequency Integer,
        Id Integer, primary_key,
        LastBillDate Date,
        LeadAffiliateId Id,
        MaxRetry Integer,
        MerchantAccountId Id,
        NextBillDate Date,
        NumDaysBetweenRetry Integer,
        OriginatingOrderId Id,
        PaidThruDate Date,
        ProductId Id,
        ProgramId Id,
        PromoCode String(250),
        Qty Integer,
        ReasonStopped String(250),
        ShippingOptionId Id,
        StartDate Date,
        Status String(250),
        SubscriptionPlanId Id
    )
    """)

tableCreators.append("""CREATE TABLE RecurringorderWithContact(
        AffiliateId Id,
        AutoCharge Integer,
        BillingAmt Float,
        BillingCycle String(250),
        CC1 Id,
        CC2 Id,
        City String(250),
        ContactId Id,
        Country String(250),
        Email String(250),
        EmailAddress2 String(250),
        EmailAddress3 String(250),
        EndDate Date,
        FirstName String(250),
        Frequency Integer,
        HTMLSignature String(250),
        LastBillDate Date,
        LastName String(250),
        LeadAffiliateId Id,
        MaxRetry Integer,
        MerchantAccountId Id,
        MiddleName String(250),
        NextBillDate Date,
        Nickname String(250),
        NumDaysBetweenRetry Integer,
        PaidThruDate Date,
        Phone1 String(250),
        Phone1Ext String(250),
        Phone1Type String(250),
        Phone2 String(250),
        Phone2Ext String(250),
        Phone2Type String(250),
        PostalCode String(250),
        ProductId Id,
        ProgramId Id,
        PromoCode String(250),
        Qty Integer,
        ReasonStopped String(250),
        RecurringOrderId Id,
        ShippingOptionId Integer,
        Signature String(250),
        SpouseName String(250),
        StartDate Date,
        State String(250),
        Status String(250),
        StreetAddress1 String(250),
        StreetAddress2 String(250),
        SubscriptionPlanId Id,
        Suffix String(250),
        Title String(250),
        ZipFour1 String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Referral(
        AffiliateId Id,
        ContactId Id,
        DateExpires Date,
        DateSet Date,
        IPAddress String(250),
        Id Integer, primary_key,
        Info String(250),
        Source String(250),
        Type Integer   Ad
    )
    """)
tableCreators.append("""CREATE TABLE Savedfilter(
        FilterName String(250),
        Id Integer, primary_key,
        ReportStoredName String(250),
        UserId String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Stage(
        Id Integer, primary_key,
        StageName String(250),
        StageOrderf Integer,
        TargetNumDays Integer
    )
    """)

tableCreators.append("""CREATE TABLE Stagemove(
        CreatedBy Id,
        DateCreated DateTime,
        Id Integer, primary_key,
        MoveDate DateTime,
        MoveFromStage Id,
        MoveToStage Id,
        OpportunityId Id,
        PrevStageMoveDate DateTime,
        UserId Id
    )
    """)

tableCreators.append("""CREATE TABLE Status(
        Id Integer, primary_key,
        StatusName String(250),
        StatusOrderf String(250),
        TargetNumDays String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Subscriptionplan(
        Active Boolean,
        Cycle String(250),
        Frequency Integer,
        Id Integer, primary_key,
        PlanPrice Float,
        PreAuthorizeAmount Float,
        ProductId Id,
        Prorate Boolean
    )
    """)
tableCreators.append("""CREATE TABLE Template(
        Categories String(250),
        Id Integer, primary_key,
        PieceTitle String(250),
        PieceType String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Ticket(
        CloseDate Date,
        ContactId Id,
        CreatedBy Id,
        DateCreated DateTime,
        DateInStage Date,
        DevId Id,
        FolowUpDate Date,
        HasCustomerCalled Integer,
        Id Integer, primary_key,
        IssueId Id,
        LastUpdated DateTime,
        LastUpdatedBy Id,
        Ordering Float,
        Priority Integer,
        Stage Id,
        Summary String(250),
        TargetCompletionDate Date,
        TicketApplication String(250),
        TicketCategory Id,
        TicketTitle String(250),
        TicketTypeId Id,
        TimeSpent Float,
        UserId Id
    )
    """)

tableCreators.append("""CREATE TABLE Ticketstage(
        Id Integer, primary_key,
        StageName String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Tickettype(
        CategoryId Id,
        Id Integer, primary_key,
        Label String(250)
    )
    """)

tableCreators.append("""CREATE TABLE User(
        City String(250),
        Email String(250),
        EmailAddress2 String(250),
        EmailAddress3 String(250),
        FirstName String(250),
        HTMLSignature String(250),
        Id Integer, primary_key,
        LastName String(250),
        MiddleName String(250),
        Nickname String(250),
        Phone1 String(250),
        Phone1Ext String(250),
        Phone1Type String(250),
        Phone2 String(250),
        Phone2Ext String(250),
        Phone2Type String(250),
        PostalCode String(250),
        Signature String(250),
        SpouseName String(250),
        State String(250),
        StreetAddress1 String(250),
        StreetAddress2 String(250),
        Suffix String(250),
        Title String(250),
        ZipFour1 String(250)
    )
    """)

tableCreators.append("""CREATE TABLE Usergroup(
        Id Integer, primary_key,
        Name String(250),
        OwnerId Id
    )
    """)

for eachTable in tableCreators:
    print eachTable
    cursor.execute(eachTable)