#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-16 14:03:02
# @Last Modified 2015-05-20
# @Last Modified time: 2015-05-20 01:18:52
import xmlrpclib
import time
import random
import urllib
import base64
import csv

from ISProduct import products
from ISTables import tables
from ISTablePermissions import permissionsTable




# Above here, imports.
############################################################
# And below, generators for basic functions





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

    def deleteRecord(self, tableName, recordId):
        return self.connection.DataService.delete(self.infusionsoftAPIKey, tableName, recordId)

    def deleteAllRecords(self, tableName):
        allRecords=self.getAllRecords(tableName, ['Id',])
        for eachresult in allRecords:
            self.deleteRecord(tableName, eachresult['Id'])

def newserver(appname, apikey):
    return ISServer(appname, apikey)

