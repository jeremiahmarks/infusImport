sampleTableHeaders=["NameID", "SKU", "GPS Manufacturer Part Number", "GPS Category", "GPS Enabled", "Name", "Product URL", "Brand", "Option Set", "Description", "Price", "Allow Purchases", "Product Availability", "Category String", "Category Details", "Product Files", "Product Images", "Meta Description", "Product Condition"]
import re
import string
import xmlrpclib
import time
import random
import urllib
import base64
import csv
import productImage
import my_pw as pw

stringTranslation=string.maketrans("asdfghjklpoiuytrewq","lpokjiuhygtfrdeswaq")
iditerator = iter(range(1,300))
appname=pw.passwords['appname']
apikey = pw.passwords['apikey']
importFile=pw.passwords['importFile']

# write a server function that creates all of the product categories locally
# then write a create productCategory function that checks if the category already exists
# with the same family path (lineage?) if it does, return that id, else
# create a new one and return its id.
tables={}
tables['ProductOptValue'] = ["Id", "IsDefault", "Label", "Name", "OptionIndex", "PriceAdjustment", "ProductOptionId", "Sku",]
tables['ProductOption'] = ["AllowSpaces", "CanContain", "CanEndWith", "CanStartWith", "Id", "IsRequired", "Label", "MaxChars", "MinChars", "Name", "OptionType", "Order", "ProductId", "TextMessage"]
tables['ProductCategory'] = ["CategoryDisplayName", "CategoryImage", "CategoryOrder", "Id", "ParentId"]
tables["ProductCategoryAssign"]=["Id","ProductCategoryId","ProductId"]
products=[]
productCatagories={}

#####
# Table Information

# ProductCategory
#
# CategoryDisplayName                                 String
# CategoryImage                                         Blob
# CategoryOrder                                      Integer
# Id                                                      Id
# ParentId                                                Id
#
# ProductCategoryAssign
# 
# Id                =Id  =Read
# ProductCategoryId =Id  =Edit Add Read
# ProductId         =Id  =Edit Add Read 


class product(object):

    def __init__(self, name):
        self.id=False
        self.name=name
        self.categories=None
        self.catStrings=[]
        self.sku=False
        self.description=False
        self.price=0.00
        self.isActive=1
        self.images=[]
        self.imageStrings=[]
        self.shortDescription=False
        self.taxable=-1
        self.cityTax=-1
        self.countryTax=-1
        self.stateTax=-1
        self.shippable=-1
        self.weight=False
        self.options=None
        self.optionsSettings=None
        self.optionsPriceChange={}
        ##self.

    def prepare(self):
        vals={}
        vals["ProductName"]=self.name
        if (self.sku):
            vals["Sku"] = self.sku
        if (self.description):
            vals["Description"] = self.description
        vals["ProductPrice"] = self.price
        if (self.isActive>=0):
            vals["Status"] = self.isActive
        if (self.shortDescription):
            vals["ShortDescription"]=self.shortDescription
        if (self.taxable>=0):
            vals["Taxable"]=self.taxable
        if (self.cityTax>=0):
            vals["CityTax"]=self.cityTax
        if (self.stateTax>=0):
            vals["StateTax"] = self.stateTax
        if (self.countryTax>=0):
            vals["CountryTax"] = self.countryTax
        if (self.shippable>=0):
            vals["Shippable"] = self.shippable
        if (self.weight):
            vals["Weight"] = self.weight
        return vals

    def getPublicPage(self):
        return "https://" + server.infusionsoftapp + ".infusionsoft.com/app/storeFront/showProductDetail?productId=" + str(self.id)

    def getInternalPage(self):
        return "https://" + server.infusionsoftapp + ".infusionsoft.com/app/product/manageProduct?productId=" + str(self.id)

class productCat(object):
    global productCatagories
    def __init__(self, name):
        self.name=name
        self.children=[]
        self.image=None
        self.order=None
        self.id=None
        self.parent=0

    def register(self):
        if self.parent in [None,0]:
            self.parent = 0
            self.path=""+self.name
        else:
            self.path=productCatagories[self.parent].path+"/"+self.name
        productCatagories[self.path]=self
        if self.id is not None:
            productCatagories[self.id]=self


    def prepare(self):
        vals={}
        vals["CategoryDisplayName"] = self.name
        if (self.order is not None):
            vals["CategoryOrder"] = self.order
        if self.parent is not None:
            vals["ParentId"] = self.parent
        if self.image is not None:
            vals["CategoryImage"]
        return vals

    def allVals(self):
        vals={}
        if self.id is not None:
            vals['Id'] = self.id
        vals.update(self.prepare)
        return vals

class prodCatAss(object):

    def __init__(self, productId, catId):
        self.pid = productId
        self.catId = catId
        self.id=None

    def prepare(self):
        vals = {}
        vals["ProductCategoryId"] = self.catId # I admit, I feel dirty using that as a variable
        vals["ProductId"] = self.pid
        return vals

    def allVals(self):
        vals={}
        if self.id is not None:
            vals['Id'] = self.id
        return vals.update(self.prepare())

class prodOption(object):

    def __init__(self, productId):
        self.ProductId = productId
        self.id=None
        self.allowSpaces=None
        self.canContain=None
        self.canEndWith=None
        self.maxChars=None
        self.minChars=None
        self.name=None
        self.label=None
        self.required=None
        self.order=None
        self.optionType=None
        self.textMessage=None
        self.values=[]

    def prepare(self):
        vals={}
        vals["ProductId"] = self.ProductId
        if self.allowSpaces is not None:
            vals["AllowSpaces"] = self.allowSpaces
        if self.canContain is not None:
            vals["CanContain"] = self.canContain
        if self.canEndWith is not None:
            vals["CanEndWith"] = self.canEndWith
        if self.maxChars is not None:
            vals["MaxChars"] = self.maxChars
        if self.minChars is not None:
            vals["MinChars"] = self.minChars
        if self.name is not None:
            vals["Name"] = self.name
        if self.label is not None:
            vals["Label"] = self.label
        if self.required is not None:
            vals["IsRequired"] = self.required
        if self.order is not None:
            vals["Order"] = self.order
        if self.optionType is not None:
            vals["OptionType"] = self.optionType
        if self.textMessage is not None:
            vals["TextMessage"] = self.textMessage
        return vals

    def allVals(self):
        vals={}
        if self.id is not None:
            vals["Id"] = self.id
        return vals.update(self.prepare())
class prodOptVal(object):

    def __init__(self, optionID):
        self.id=None
        self.optionID = optionID
        self.label=None
        self.sku=None
        self.isdefault=None
        self.name=None
        self.optionIndex=None
        self.adjustment=None

    def prepare(self):
        vals={}
        vals["ProductOptionId"] = self.optionID
        if self.label is not None:
            vals["Label"] = self.label
        if self.sku is not None:
            vals["Sku"] = self.sku
        if self.isdefault is not None:
            vals["IsDefault"] = self.isdefault
        if self.name is not None:
            vals["Name"] = self.name
        if self.optionIndex is not None:
            vals["OptionIndex"] = self.optionIndex
        if self.adjustment is not None:
            vals["PriceAdjustment"] = self.adjustment
        return vals

    def allVals(self):
        vals={}
        if self.id is not None:
            vals["Id"] = self.id
        return vals.update(self.prepare())
class ISServer:
    def __init__(self, infusionsoftapp, infusionsoftAPIKey):
        self.infusionsoftapp=infusionsoftapp
        self.infusionsoftAPIKey=infusionsoftAPIKey
        self.appurl = "https://" + self.infusionsoftapp + ".infusionsoft.com:443/api/xmlrpc"
        self.connection = xmlrpclib.ServerProxy(self.appurl)

    def getTagCats(self):
        self.tagcats={}
        p=0
        while True:
            listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, "ContactGroupCategory", 1000, p, {}, ['Id', 'CategoryName'], 'CategoryName',True)
            for eachCat in listOfDicts:
                self.tagcats[eachCat['Id']] = eachCat['CategoryName']
            if not(len(listOfDicts)==1000):
                break
            p=p+1

    def getAllTags(self):
        self.tags={}
        p=0
        while True:
            listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, "ContactGroup", 1000,p,{},['Id',"GroupCategoryId","GroupName"],"GroupName", True )
            for eachtag in listOfDicts:
                if not (eachtag.has_key('GroupName')):
                    eachtag['GroupName']=""
                self.tags[eachtag['Id']]=(ISTag(eachtag['Id'], eachtag['GroupName'], eachtag['GroupCategoryId']))
            if not(len(listOfDicts)==1000):
                break
            p=p+1

    def prep(self):
        self.getTagCats()
        self.getAllTags()

    def getContactsWithTag(self, startdate="19000101T00:00:00", enddate="30001231T23:59:59", tagID=303):
        records=[]
        sdate = time.strptime(startdate, '%Y%m%dT%H:%M:%S')
        edate = time.strptime(enddate, '%Y%m%dT%H:%M:%S')
        p=0
        while True:
            listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, 'ContactGroupAssign', 1000,p,{'GroupId':tagID},['Contact.Email', 'Contact.FirstName', 'Contact.LastName', 'Contact.Id', 'DateCreated'],"Contact.Id",True)
            for eachApplication in listOfDicts:
                datetimeapplied = time.strptime(eachApplication['DateCreated'].value, '%Y%m%dT%H:%M:%S')
                if ((datetimeapplied>=sdate) and (datetimeapplied<=edate)):
                    interestingData = ["Contact.FirstName", "Contact.LastName", 'Contact.Email']
                    for eachbit in interestingData:
                        if not eachApplication.has_key(eachbit):
                            eachApplication[eachbit]=None
                    records.append(TagAppliedRecord(eachApplication['Contact.Id'],eachApplication['Contact.FirstName'],eachApplication['Contact.LastName'],eachApplication['Contact.Email'], self.tags[tagID].name, tagID, datetimeapplied))
            if not(len(listOfDicts)==1000):
                break
            p=p+1
        return records

    def getContactIDWithTag(self, tagID):
        records = []
        p=0
        while True:
            listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'ContactGroupAssign', 1000,p,{'GroupId':tagID}, ['Contact.Id', 'Contact.FirstName', 'Contact.LastName', 'Contact.Email' ], 'Contact.Id', True)
            for eachContact in listOfDicts:
                interestingData = ["Contact.FirstName", "Contact.LastName", 'Contact.Email']
                for eachbit in interestingData:
                    if not eachContact.has_key(eachbit):
                        eachContact[eachbit]=None
                records.append(BasicContact(eachContact['Contact.Id'], fname=eachContact['Contact.FirstName'], lname=eachContact['Contact.LastName'], emailAddress=eachContact['Contact.Email']))
            if not(len(listOfDicts)==1000):
                break
            p+=1
        return records

    def getAllContacts(self):
        records = []
        p=0
        while True:
            listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'Contact', 1000,p,{},['Id', 'FirstName', 'LastName', 'Email'], 'Id', True)
            for eachContact in listOfDicts:
                interestingData=['FirstName',"LastName",'Email']
                for eachbit in interestingData:
                    if not eachContact.has_key(eachbit):
                        eachContact[eachbit]=None
                records.append(BasicContact(eachContact['Id'], fname=eachContact['FirstName'], lname=eachContact['LastName'], emailAddress=eachContact['Email']))
            if not(len(listOfDicts)==1000):
                break
            p+=1
        return records

    def verifyConnection(self):
        try:
            listOfDicts=self.connection.DataService.query(self.infusionsoftAPIKey, "User", 1000, 0,{},["Email"],"Email",True)
            return True
        except:
            return False

    def getCount(self, tableName, query):
        return self.connection.DataService.count(self.infusionsoftAPIKey, tableName, query)

    def createNewTag(self, newTagName):
        return self.connection.DataService.add(self.infusionsoftAPIKey, 'ContactGroup', {'GroupName':newTagName})

    def createNewRecord(self, table, productValues):
        return self.connection.DataService.add(self.infusionsoftAPIKey, table, productValues)

    def cnp(self, proVals):
        return self.connection.DataService.add(self.infusionsoftAPIKey, 'Product', proVals)

    def addTagToContact(self, contactID, tagID):
        self.connection.ContactService.addToGroup(self.infusionsoftAPIKey, contactID, tagID)

    def deleteTag(self, tagID):
        self.connection.DataService.delete(self.infusionsoftAPIKey, 'ContactGroup', tagID)

    def placeOrder(self, contactID, creditCardId, payPlanId, productIds, subscriptionPlanIds, processSpecials, promoCodes, leadAffiliateId, saleAffiliateId):
        return self.connection.OrderService.placeOrder(self.infusionsoftAPIKey, int(contactID), int(creditCardId), int(payPlanId), productIds, subscriptionPlanIds, processSpecials, promoCodes, leadAffiliateId, saleAffiliateId)

    def getContactsWithCards(self):
        records=[]
        p=0
        while True:
            listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'CreditCard', 1000,p,{},['Id', 'ContactId', 'Email','FirstName', 'LastName', 'Last4'], 'Id', True)
            for each in listOfDicts:
                interestingData=["Id", 'ContactId', 'Email','FirstName', 'LastName', 'Last4']
                if not(each.has_key('Email') or each.has_key('FirstName') or each.has_key('LastName')):
                    pass
                else:
                    for eachbit in interestingData:
                        if not each.has_key(eachbit):
                            each[eachbit]=None
                    records.append(ContactWithCreditCard(each['Id'], each['Last4'],each['ContactId'], each['FirstName'], each['LastName'], each['Email'] ))
            if not(len(listOfDicts)==1000):
                break
            p+=1
        return records

    def getAllProducts(self):
        records=[]
        p=0
        while True:
            listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'Product', 1000, p, {}, ['Id', 'ProductName', 'ProductPrice', 'ShippingTime', 'IsPackage', 'HideInStore'], 'Id', True)
            for each in listOfDicts:
                interestingData=['ProductName', 'ProductPrice', 'ShippingTime', 'IsPackage', 'HideInStore']
                for eachbit in interestingData:
                    if not each.has_key(eachbit):
                        each[eachbit]=None
                records.append((each['Id'], each['ProductName'], each['ProductPrice'], each['ShippingTime'], each['IsPackage'], each['HideInStore']))
            if not(len(listOfDicts)==1000):
                break
            p+=1
        return records

    def getAllProductCats(self):
        records = []
        p=0
        interestingData=["CategoryDisplayName", "CategoryImage", "CategoryOrder", "Id", "ParentId"]
        while True:
            listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, 'ProductCategory', 1000,p,{}, interestingData, 'Id', True)
            for eachProCat in listOfDicts:
                thisCat={}
                for eachbit in interestingData:
                    if not eachProCat.has_key(eachbit):
                        eachProCat[eachbit]=None
                    thisCat[eachbit] = eachProCat[eachbit]
                records.append(thisCat)
            if not(len(listOfDicts)==1000):
                break
            p+=1
        return records

    def getAllRecords(self, tableName, interestingData, orderedBy=None):
        if orderedBy is None:
            orderedBy = interestingData[0]
        records = []
        p=0
        # interestingData=["AllowSpaces", "CanContain", "CanEndWith", "CanStartWith", "Id", "IsRequired", "Label", "MaxChars", "MinChars", "Name", "OptionType", "Order", "ProductId", "TextMessage"]
        while True:
            listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, tableName, 1000, p, {}, interestingData, orderedBy, True)
            for each in listOfDicts:
                thisRecord={}
                for eachbit in interestingData:
                    if not each.has_key(eachbit):
                        each[eachbit]=None
                    thisRecord[eachbit] = each[eachbit]
                records.append(thisRecord)
            if not(len(listOfDicts)==1000):
                break
            p+=1
        return records

    def updateRecord(self, tableName, recordId, updateValues):
        return self.connection.DataService.update(self.infusionsoftAPIKey, tableName, recordId, updateValues)

    def getMatchingRecords(self, tableName, criteria, desiredFields, orderedBy=None):
        if orderedBy is None:
            orderedBy = desiredFields[0]
        records = []
        p=0
        # interestingData=["AllowSpaces", "CanContain", "CanEndWith", "CanStartWith", "Id", "IsRequired", "Label", "MaxChars", "MinChars", "Name", "OptionType", "Order", "ProductId", "TextMessage"]
        while True:
            listOfDicts = self.connection.DataService.query(self.infusionsoftAPIKey, tableName, 1000, p, criteria, desiredFields, orderedBy, True)
            for each in listOfDicts:
                thisRecord={}
                for eachbit in desiredFields:
                    if not each.has_key(eachbit):
                        each[eachbit]=None
                    thisRecord[eachbit] = each[eachbit]
                records.append(thisRecord)
            if not(len(listOfDicts)==1000):
                break
            p+=1
        return records


    def addImageToProduct(self, productID, image):
        return self.connection.DataService.update(self.infusionsoftAPIKey, 'Product', {'ShortDescription' : 'Updated with new image'})
server=ISServer(appname, apikey)
def buildCategories(force=False):
    global productCatagories
    global server
    global tables
    if (len(productCatagories)==0 or force):
        allCategories=server.getAllRecords('ProductCategory', tables['ProductCategory'])
        catHold=[]
        for eachCategory in allCategories:
            print eachCategory
            thisCat = productCat(eachCategory['CategoryDisplayName'])
            thisCat.id=eachCategory['Id']
            if eachCategory["ParentId"] is not None:
                thisCat.parent=eachCategory["ParentId"]
            if eachCategory["CategoryImage"] is not None:
                thisCat.CategoryImage=eachCategory["CategoryImage"]
            if eachCategory["CategoryImage"] is not None:
                thisCat.order=eachCategory["CategoryImage"]
            catHold.append(thisCat)
        for eachCat in [cat for cat in catHold if cat.parent in[None,0]]:
            print "ee each"
            eachCat.register()
        while True:
            repeat=False
            for eachCategory in catHold:
                try:
                    eachCategory.register()
                except KeyError:
                    print KeyError.args
                    print KeyError.message
                    #repeat=True
            if not repeat:
                break


def getCatId(pathToCat):
    global productCatagories
    global iditerator
    global server

    print "Catgs buil"
    buildCategories()
    print "Catgs built"
    checkPath = '/'+pathToCat
    # if (checkPath[0] != '/'):
    #     checkPath = '/' + pathToCat
    if pathToCat in productCatagories.keys():
        return productCatagories[pathToCat].id
    else:
        pathData=pathToCat.rsplit('/',1)
        if len(pathData)==1:
            thisCat = productCat(pathData[0])
        else:
            thisCat = productCat(pathData[1])
            thisCat.parent=getCatId(pathData[0])
        thisCat.id=server.createNewRecord('ProductCategory', thisCat.prepare())
        thisCat.register()
        return thisCat.id

def getCatAssiggnId(productCatAssRecord):
    global server
    global tables
    matchingRecords=server.getMatchingRecords( "ProductCategoryAssign", productCatAssRecord.prepare(), tables["ProductCategoryAssign"])
    if len(matchingRecords)>0:
        return matchingRecords[0]["Id"]
    else:
        return server.createNewRecord("ProductCategoryAssign", productCatAssRecord.prepare())



def parseOptions(optionString,sku=None, pricing=None, currentProductOptions={}):
    originalOptionString=optionString
    numberOfOptionTypes=optionString.count('[')
    optionType=''
    if numberOfOptionTypes==0:
        optionType="skuPricing"
        optionValues="skuPricing"
        numberOfOptionTypes=1
    knownOptionTypes = ['RT', 'RB', 'CS']
    options={}
    if pricing is not None:
        pricingOptions=re.split(r"[\[|,^\]]",pricing)
        print "Pricing ", pricingOptions
        if 'REMOVE' in pricingOptions:
            priceChange=float(pricingOptions[2])*-1
        elif len(pricingOptions)>1:
            priceChange=pricingOptions[2]
        else:
            priceChange=None
    for eachType in range(numberOfOptionTypes):
        if optionType is not "skuPricing":
            optionType=optionString[1:3]
            # print optionType
            try:
                nextTypeStart=optionString.find('[',4)
                optionValues=optionString[4:]
                optionString = optionString[nextTypeStart:]
            except IndexError:
                optionValues=optionString[4:]
                optionString=''
                print IndexError
        if optionType not in options.keys():
            options[optionType]=[]
        options[optionType].append(optionValues)
    for optionType in options.keys():
        for eachString in options[optionType]:
            eachString=eachString.strip(', ')
            for eachOptionDatum in re.split(r"[\[|,^\]]*",eachString):
                # print eachOptionDatum
                if (len(eachOptionDatum)>0):
                    segmentedList=re.split(r"[,=:]",eachOptionDatum)
                    if (len(segmentedList)>1):
                        if segmentedList[0] not in currentProductOptions.keys():
                            currentProductOptions[segmentedList[0]]={'pricing': {}, 'options': set(), 'skud': {} }
                        currentProductOptions[segmentedList[0]]['options'].add(segmentedList[1])
                        if sku is not None:
                            if segmentedList[1] not in currentProductOptions[segmentedList[0]]['skud'].keys():
                                currentProductOptions[segmentedList[0]]['skud'][segmentedList[1]]=[sku]
                            else:
                                currentProductOptions[segmentedList[0]]['skud'][segmentedList[1]].append(sku)
                    if priceChange is not None:
                            print priceChange
                            currentProductOptions[segmentedList[0]]['pricing'][segmentedList[1]]=priceChange

    return currentProductOptions

def getRowType(row):
        if len(row["Name"]) is 0:
            return "skuPricing"
        elif (row["Name"][0] is not "["):
            return "product"
        elif (len(row["SKU"])==0):
            return "pricingRule"
        else:
            return "option"


def sampleData(productsExport=pw.passwords['importFile']):
    global server
    global products
    global productCatagories
    server = ISServer(appname, apikey)
    with open(productsExport) as datas:
        reader = csv.DictReader(datas)
        for row in reader:
            rowType=getRowType(row)
            if rowType=="product":
                print "A product!"
                print row["Name"]
                thisProduct = product(row["Name"])
                thisProduct.optionsTree={}
                thisProduct.options={}
                products.append(thisProduct)
                for column in ["GPS Category", "Brand", "Category String"]:
                    if (len(row[column])):
                        thisProduct.catStrings.append(row[column].replace("\xe2\x84\xa2","TM"))
                if row["SKU"]:
                    thisProduct.sku = row["SKU"]
                if row['Description']:
                    thisProduct.description=row['Description']
                if row["Price"]:
                    thisProduct.price = row["Price"]
                if row["Product Images"]:
                    thisProduct.imageStrings.append(row["Product Images"])
                if row["Meta Description"]:
                    thisProduct.shortDescription = row["Meta Description"]
                if row["Product Images"]:
                    imageStrings=row["Product Images"].split("|")
                    for eachS in imageStrings:
                        for eachVal in eachS.split(","):
                            if "Product Image URL: " in eachVal:
                                thisProduct.images.append(eachVal.replace("Product Image URL: ","").strip())
                thisProduct.id = server.cnp(thisProduct.prepare())
                    # if rowType=="option":
                    #     thisProduct.optionRows.append(row)
                    # elif rowType=="skuPricing":
                    #     thisProduct.skuRuleRows.append(row)
                    # elif rowType=="pricingRule":
                    #     thisProduct.pricingRows.append(row)
            else:
                thisProduct.optionsTree=parseOptions(row["Name"],sku=row["SKU"], pricing=row["Price"], currentProductOptions=thisProduct.optionsTree)
                #     return products
                # def continuee():
                #     if True:
        for eachProduct in products:
            print "parsing some prods!"
        # def workaProduct(eachProduct):
            optionOrder=0
            for eachOption in eachProduct.optionsTree.keys():
                print eachOption
                if eachOption is None:
                    eachOption="skuPricing"
                optionOrder+=1
                thisOption = prodOption(eachProduct.id)
                thisOption.name=eachOption
                thisOption.label = eachOption
                thisOption.required = 1
                thisOption.order = optionOrder
                thisOption.optionType='FixedList'
############################################################
## Update the below to make sure that it checks for existence 
## prior to creation, I am pretty sure that it does not currently
                thisOption.id = server.createNewRecord("ProductOption", thisOption.prepare())
                print thisOption.id
                # thisOption.id=iditerator.next()
                eachProduct.options[eachOption] = thisOption
                optionCounter=0
                for eachValue in list(eachProduct.optionsTree[eachOption]['options']):
                    optionCounter+=1
                    print "Each value checking in", eachValue
                    newOptionValue=prodOptVal(thisOption.id)
                    newOptionValue.optionIndex=optionCounter
                    newOptionValue.label = eachValue
                    newOptionValue.isdefault=0
                    newOptionValue.name=eachValue
                    if eachValue in eachProduct.optionsTree[eachOption]['pricing'].keys():
                        newOptionValue.adjustment=eachProduct.optionsTree[eachOption]['pricing']
                    elif eachValue in eachProduct.optionsTree[eachOption]['skud'].keys():
                        mysku=eachProduct.optionsTree[eachOption]['skud'][eachValue]
                        newOptionValue.adjustment=eachProduct.optionsTree[eachOption]['pricing'][mysku]
                    newOptionValue.id = server.createNewRecord("ProductOptValue", newOptionValue.prepare())
                    # newOptionValue.id = iditerator.next()
                    thisOption.values.append(newOptionValue)
            for eachString in eachProduct.catStrings:
                print eachString
                if eachProduct.categories is None:
                    eachProduct.categories={}
                eachString.replace("\\/", "___")
                for eachSubstring in eachString.split(";"):
                    print "substring ", eachSubstring
                    thiscatid=getCatId(eachSubstring)
                    print "catid", thiscatid
                    thisAssignment=prodCatAss(eachProduct.id, thiscatid)
                    
                    thisAssignment.id=getCatAssiggnId(thisAssignment)
                    print "this assignment"
                    eachProduct.categories[eachSubstring]=eachProduct.categories[int(thiscatid)]=thisAssignment
    return products


##  
##  
##  
##  
##  ##################################################################
##  ##################################################################
        ##  #            if (row["Name"] and row["Name"][0]=="["):
        ##  #                # This indicates that it is not a product
        ##  #                # if (row["Price"]==""):
        ##  #                    # If the price value is blank, this means
        ##  #                    # that it is an option, not a pricing rule
        ##  #                optionString=row["Name"]
        ##  #                optionString = optionString[4:].replace("\\,","_-_")
        ##  #                while(len(optionString)>0):
        ##  #                    if thisProduct.optionsSettings is None:
        ##  #                        thisProduct.optionsSettings={}
        ##  #                    optionType, optionString=optionString[1:3], optionString[4:]
        ##  #                    nextOptionStart=optionString.find('[')
        ##  #                    if (nextOptionStart>0):
        ##  #                        currentOptions,optionString = optionString[:nextOptionStart], optionString[nextOptionStart:]
        ##  #                    else:
        ##  #                        currentOptions,optionString=optionString,''
        ##  #                    # if (optionType=='RB'):
        ##  #                    try:
        ##  #                        theseOptions = currentOptions.split(',')
        ##  #                    except ValueError:
        ##  #                        theseOptions = [currentOptions,]
        ##  #                    for eachOption in theseOptions:
        ##  #                        print eachOption
        ##  #                        try:
        ##  #                            optionName,optionValue=eachOption.split("=")
        ##  #                            optionName = optionName.replace("_-_",",")
        ##  #                        except:
        ##  #                            optionName,optionValue=eachOption,"Whoops!"
        ##  #                        if optionName not in thisProduct.optionsSettings.keys():
        ##  #                            thisProduct.optionsSettings[optionName] = set()
        ##  #                        colonPlace=eachOption.find(':')
        ##  #                        if (colonPlace>0):
        ##  #                            eachOption = eachOption[:colonPlace]
        ##  #                        thisProduct.optionsSettings[optionName]=''.join(optionValue)
        ##  #                    # if (optionType=='CS'):
        ##  #                        # pass
        ##  #
        ##  #                    This should remove the original tag
        ##  #                    # optionName, optionString = optionString.split("=",1)
        ##  #                    # if thisProduct.optionsSettings is None:
        ##  #                        # thisProduct.optionsSettings={}
        ##  #                    # if optionName not in thisProduct.optionsSettings.keys():
        ##  #                        # thisProduct.optionsSettings[optionName.replace("_-_",",")] = set()
        ##  #                    # try:
        ##  #                        # optionsValue, optionString = optionString.split(",",1)
        ##  #                    # except ValueError:
        ##  #                        # optionsValue = optionString
        ##  #                        # optionString = ""
        ##  #                    # thisProduct.optionsSettings[optionName].add(optionsValue)
        ##  #                if (len(row["Price"])>0):
        ##  #                    #################################################################################
        ##  #                    #################################################################################
        ##  #                    # This is a pricing rule
        ##  #                    priceOptionSeperator=row["Price"].find(']')
        ##  #                    priceChangeType, priceChange = row["Price"][:priceOptionSeperator].replace('[','').replace(']',''), row["Price"][priceOptionSeperator+1:]
        ##  #                    print str(thisProduct.id) + " ::: options " + priceChangeType + "  ::::" + priceChange
        ##  #                    if priceChangeType=="REMOVE":
        ##  #                        priceChange = str(-1*float(priceChange))
        ##  #                    optionChoice, optionChoiceValue = row["Name"][row["Name"].find(']')+1:].split("=",1)
        ##  #                    for eachS in [optionChoice, optionChoiceValue, priceChangeType, priceChange]:
        ##  #                        print eachS
        ##  #                    if thisProduct.optionsPriceChange is None:
        ##  #                        thisProduct.optionsPriceChange={}
        ##  #                    if optionChoice not in thisProduct.optionsPriceChange.keys():
        ##  #                        thisProduct.optionsPriceChange[optionChoice]={}
        ##  #                    thisProduct.optionsPriceChange[optionChoice][optionChoiceValue] = priceChange
        ##  #            else:
        ##  #                # this is a product
        ##  #                if thisProduct is not None:
        ##  #                    # This is to save the just completed product.
        ##  #                    # so that we can access it later, and assign its variable to
        ##  #                    # a different object. (Okay, really assign a different object
        ##  #                    # to this variable ) We do not want to call it before the first
        ##  #                    # product is created, hence the if to check.
        ##  #                    products.append(thisProduct)
        ##  #                thisProduct = product(row["Name"])
        ##  #                if (thisProduct.name=="" or thisProduct.name==None ):
        ##  #                    continue
        ##  #                for column in ["GPS Category", "Brand", "Category String"]:
        ##  #                    if (len(row[column])):
        ##  #                        thisProduct.catStrings.append(row[column].replace("\xe2\x84\xa2","TM"))
        ##  #                if row["SKU"]:
        ##  #                    thisProduct.sku = row["SKU"]
        ##  #                if row['Description']:
        ##  #                    thisProduct.description=row['Description']
        ##  #                if row["Price"]:
        ##  #                    thisProduct.price = row["Price"]
        ##  #                if row["Product Images"]:
        ##  #                    thisProduct.imageStrings.append(row["Product Images"])
        ##  #                if row["Meta Description"]:
        ##  #                    thisProduct.shortDescription = row["Meta Description"]
        ##  #                if row["Product Images"]:
        ##  #                    imageStrings=row["Product Images"].split("|")
        ##  #                    for eachS in imageStrings:
        ##  #                        for eachVal in eachS.split(","):
        ##  #                            if "Product Image URL: " in eachVal:
        ##  #                                thisProduct.images.append(eachVal.replace("Product Image URL: ","").strip())
        ##  #                thisProduct.id = server.cnp(thisProduct.prepare())
        ##  #                # thisProduct.id=iditerator.next()
    ##  # we need to save the last product somewhere after it gets created.
    ##  ####
    ##  ##
    ##  # Products have been created and have their optionsp set up.
    ##  # Let's create the actual optionsp.
    ##  for eachProduct in products:
        ##  if eachProduct.optionsSettings:
            ##  if eachProduct.options is None:
                ##  eachProduct.options = {}
            ##  counter=0
            ##  for eachOption in eachProduct.optionsSettings.keys():
                ##  counter+=1
                ##  thisOption = prodOption(eachProduct.id)
                ##  thisOption.name=eachOption
                ##  thisOption.label = eachOption
                ##  thisOption.required = 1
                ##  thisOption.order = counter
                ##  thisOption.optionType='FixedList'
                ##  thisOption.id = server.createNewRecord("ProductOption", thisOption.prepare())
                ##  # thisOption.id=iditerator.next()
                ##  eachProduct.options[eachOption] = thisOption
                ##  optionCounter=0
                ##  for eachValue in eachProduct.optionsSettings[eachOption]:
                    ##  optionCounter+=1
                    ##  newOptionValue=prodOptVal(thisOption.id)
                    ##  newOptionValue.optionIndex=optionCounter
                    ##  newOptionValue.label = eachValue
                    ##  newOptionValue.isdefault=0
                    ##  newOptionValue.name=eachValue
                    ##  if eachOption in eachProduct.optionsPriceChange.keys():
                        ##  if eachValue in eachProduct.optionsPriceChange[eachOption].keys():
                            ##  newOptionValue.adjustment=eachProduct.optionsPriceChange[eachOption][eachValue]
                    ##  newOptionValue.id = server.createNewRecord("ProductOptValue", newOptionValue.prepare())
                    ##  # newOptionValue.id = iditerator.next()
                    ##  thisOption.values.append(newOptionValue)
        ##  print "prod ops complete"
        ##  # each product option has been created and assigned.
        ##  # lets take care of the categories.
        ##  for eachString in eachProduct.catStrings:
            ##  if eachProduct.categories is None:
                ##  eachProduct.categories={}
            ##  eachString.replace("\\/", "___")
            ##  for eachSubstring in eachString.split(";"):
                ##  #The string should now be something like
                ##  # ParentCat/ChildCat/grandChildCat
                ##  thiscatid=getCatId(eachSubstring)
                ##  thisAssignment=prodCatAss(eachProduct.id, thiscatid)
                ##  thisAssignment.id=getCatAssiggnId(thisAssignment)
                ##  eachProduct.categories[eachSubstring]=eachProduct.categories[int(thiscatid)]=thisAssignment
        ##  # if eachProduct.images:
        ##  #     productImage.addImageToProduct(eachProduct.id, eachProduct.images[0])
    ##  return products