#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-15 19:49:25
# @Last Modified 2015-05-16
# @Last Modified time: 2015-05-16 13:07:57

##InfusionsoftImportMonster
##Basically everything in one file

############################################################
###  Shortcut:  ctrl +k ctrl+1 to fold all
############################################################

## Also: note to self, if it is not running:
    ## check the first line, you big dummy


import xmlrpclib
import time
import random
import urllib
import base64
import csv
import my_pw as pw

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





class product(object):

    def __init__(self, name):
        self.id=False
        self.name=name
        self.categories=False
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
    def __init__(self, name):
        self.name=name
        self.children=[]
        self.image=None
        self.order=None
        self.id=None
        self.parent=None

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

    def addImageToProduct(self, productID, image):
        return self.connection.DataService.update(self.infusionsoftAPIKey, 'Product', {'ShortDescription' : 'Updated with new image'})

def addToCategories(productId, categoryString):
    global productCatagories
    # basically the string will be expected to be a filepath
    # of categories.  IE: 'cat1/cat2/'. Heck that is a neat idea
    # categoryPathAt = 
    categoryPath=iter(categoryString.split("/"))
    objectPath=[] # if the path were a/b/c, this will hold the 
    stringPath=""
    # object representation of that path
    #for eachCatPos in range(len(categoryPath)):
        # the product categories are stored in a global 
        # dictionary built like the following:
        # productCategory={
        #    "name":[
            #           TheActualProduct,
            #           {
            #           "childName":[
            #                           childProduct,
            #                       ]
            #           }
        #           ]
        # Sigh, I was trying hard not to use this iteration
        # method, but it seems like in range() is going to 
        # work best to iterate a channel of things like this
        # 
        # 
        # Sample data structure
        # 
        # check the zeroth row for zerothproductCatName
        # check the matchingElements
        # productCategory["Category1"][0] == the actual object, if it exists
        # productCategory["Category1"][1] == {
        #                                         "childName":[childProduct, 
        #                                             {
        #                                                 "childName": [
        #                                                     childProduct
        #                                                 ]
        #                                             } 
        #                                         ], 
        #                                         "otherName":[otherChildProduct,
        #                                             {
        #                                                 "child1":[child1],
        #                                                 "child2":[child2]
        #                                             }
        #                                         ]
        #                                     }
        #categoryName = categoryPath[eachCatPos]
        #stringPath +=categoryName
        # we are going to make sure we register children with 
        # their parents when we are building this, so that 
        # they can all be found from top down at all time. 
        # step through the global list of objects to find the 
        # parent of the current.  See if your name is listed as
        # a child. If it is, return your object. If it is not, 
        # create a key pointing to you at #0 your way. Your children
        # will be at #1, by the way.
        # use list[:-1] to snag the last one. 
        # path = "" + OtherPathsUsingIterator + "/"
        # should make the global naming convention easy.
        # Actual file is stored in global["Potentialpath"]["/"] and
        # children are stored in global ["path/"]
        # if categoryName in productCatagories.keys()
        # productCatagories[stringPath]={'/':categoryPath[eachCatPos],
        #                             categoryName:{}
        #

        for partialPath in categoryPath:
            stringtopath+=potpath
            rD[stringtopath]=stringtopath
            stringtopath+='/'
    return productCatagories


def sampleData(productsExport=pw.passwords['importFile']):
    global server
    global products
    blankProd=product("")
    server = ISServer(appname, apikey)
    thisProduct=None
    with open(productsExport) as datas:
        reader = csv.DictReader(datas)
        for row in reader:
            if (row["Name"][0]=="["):
                #This indicates that it is not a product
                if (row["Price"]==""):
                    # If the price value is blank, this means
                    # that it is an option, not a pricing rule
                    optionString=row["Name"]
                    while(len(optionString)>0):
                        optionString = optionString[4:]
                        # This should remove the original tag
                        optionName, optionString = optionString.split("=",1)
                        if thisProduct.optionsSettings is None:
                            thisProduct.optionsSettings={}
                        if optionName not in thisProduct.optionsSettings.keys():
                            thisProduct.optionsSettings[optionName] = set()
                        try:
                            optionsValue, optionString = optionString.split(",",1)
                        except ValueError:
                            optionsValue = optionString
                            optionString = ""
                        thisProduct.optionsSettings[optionName].add(optionsValue)
                else:
                    # This is a pricing rule
                    priceChange = row["Price"][5:]
                    optionChoice, optionChoiceValue = row["Name"][4:].split("=",1)
                    if thisProduct.optionsPriceChange is None:
                        thisProduct.optionsPriceChange={}
                    if optionChoice not in thisProduct.optionsPriceChange.keys():
                        thisProduct.optionsPriceChange[optionChoice]={}
                    thisProduct.optionsPriceChange[optionChoice][optionChoiceValue] = priceChange
            else:
                #this is a product
                if thisProduct is not None:
                    # This is to save the just completed product. 
                    # so that we can access it later, and assign its variable to 
                    # a different object. (Okay, really assign a different object
                    # to this variable ) We do not want to call it before the first
                    # product is created, hence the if to check.
                    products.append(thisProduct)
                thisProduct = product(row["Name"])
                for column in ["GPS Category", "Brand", "Category String"]:
                    thisProduct.catStrings.append(row[column])
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
                thisProduct.id = server.cnp(thisProduct.prepare())
                # thisProduct.id=iditerator.next()
    # we need to save the last product somewhere after it gets created. 
    products.append(thisProduct)
    ####
    ##
    # Products have been created and have their optionsp set up.
    # Let's create the actual optionsp.
    for eachProduct in products:
        if eachProduct.optionsSettings:
            if eachProduct.options is None:
                eachProduct.options = {}
            counter=0
            for eachOption in eachProduct.optionsSettings.keys():
                counter+=1
                thisOption = prodOption(eachProduct.id)
                thisOption.name=eachOption
                thisOption.label = eachOption
                thisOption.required = 1
                thisOption.order = counter
                thisOption.optionType='FixedList'
                thisOption.id = server.createNewRecord("ProductOption", thisOption.prepare())
                # thisOption.id=iditerator.next()
                eachProduct.options[eachOption] = thisOption
                optionCounter=0
                for eachValue in eachProduct.optionsSettings[eachOption]:
                    optionCounter+=1
                    newOptionValue=prodOptVal(thisOption.id)
                    newOptionValue.optionIndex=optionCounter
                    newOptionValue.label = eachValue
                    newOptionValue.isdefault=0
                    newOptionValue.name=eachValue
                    if eachOption in eachProduct.optionsPriceChange.keys():
                        if eachValue in eachProduct.optionsPriceChange[eachOption].keys():
                            newOptionValue.adjustment=eachProduct.optionsPriceChange[eachOption][eachValue]
                    newOptionValue.id = server.createNewRecord("ProductOptValue", newOptionValue.prepare())
                    # newOptionValue.id = iditerator.next()
                    thisOption.values.append(newOptionValue)
        # each product option has been created and assigned. 
        # lets take care of the categories.
        for eachString in eachProduct.catStrings:
            eachString.replace("\\", "")
            for eachSubstring in eachString.split(";"):
                #The string should now be something like
                # ParentCat/ChildCat/grandChildCat
                pass




    return products