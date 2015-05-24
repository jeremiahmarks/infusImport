#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-22 20:20:29
# @Last Modified 2015-05-23
# @Last Modified time: 2015-05-23 18:49:35


# A collection of functions to work with an Infusionsoft
# application via the api
import os
import ISTableObjects
import ISTables
import datetime
import csv
##
# To-do: make a csv template file generator,
# or the other way around, assist a user in
# matching columns between various csv files
# and the records already on the server.
#
# To-Do: add logfilewriter to server


class serverWorker(object):
    """
    ########################################################
    ## newWorker=serverWorker(ISServer(appName, apikey))
    ## List of functions:
    ##      serverWorker.delAll(tablename) - deletes everything it can from the table
    ##      serverWorker.getAll(tablename) - returns all values from the table
    ##      serverWorker.writer("A string") - writes \"A String\" to the logfile 
    """
    global writer
    def delAll(self, tablename):
        """
        delAll accepts a tablename. It then checks that the tablename
        is approved for it to delete, and it does. 
        """
        delAlltimestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        delAllFolder=os.path.join(os.path.dirname(self.files["logfilefilePath"]), "delAll")
        if not os.path.isdir(delAllFolder):
            os.makedirs(delAllFolder)
        if "delAllWriterPath" not in self.files.keys():
            self.files["delAllWriterPath"]={}
        self.files["delAllWriterPath"][tablename]=os.path.join(delAllFolder, delAlltimestamp + "_"  + tablename + ".csv")
        delAllWriterFile=open(self.files["delAllWriterPath"][tablename],'wb+')
        delAllWriter=csv.DictWriter(delAllWriterFile, ISTables.tables[tablename], delimiter=',')
        delAllWriter.writeheader()
        #Setting up a way to store the results locally to reduce
        #Use of the API
        self.logfile=open(self.files["logfilefilePath"], 'a' )
        self.logfilewriter=self.logfile.write
        self.allExisting[tablename]={}
        rowhead=', '.join(['\n','delAll',tablename,datetime.datetime.now().strftime('%Y%m%d%H%M%S')])
        allRecords = self.server.getAllRecords(tablename, ISTables.tables[tablename] )
        delAllWriter.writerows(allRecords)
        delAllWriterFile.close()
        returnVal=allRecords
        for eachresult in allRecords:
            rowText=[]
            for colName in eachresult.keys():
                rowText+=[colName, eachresult[colName]]
            self.server.deleteRecord(tablename, eachresult['Id'])
            self.logfilewriter(', '.join([rowhead, 'deleted', ''.join(str(rowText))]))
        self.logfile.close()

    def getAll(self, tablename):
        """
        getAll accepts a table name and will return all values
        from that table. It will return them in a list of dictionaries.
        """
        getAlltimestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        getAllFolder=os.path.join(os.path.dirname(self.files["logfilefilePath"]), "getAll")
        if not os.path.isdir(getAllFolder):
            os.makedirs(getAllFolder)
        if "getAllWriterPath" not in self.files.keys():
            self.files["getAllWriterPath"]={}
        self.files["getAllWriterPath"][tablename]=os.path.join(getAllFolder, getAlltimestamp + "_"  + tablename + ".csv")
        getAllWriterFile=open(self.files["getAllWriterPath"][tablename],'wb+')
        getAllWriter=csv.DictWriter(getAllWriterFile, ISTables.tables[tablename], delimiter=',')
        getAllWriter.writeheader()
        #Setting up a way to store the results locally to reduce
        #Use of the API
        self.logfile=open(self.files["logfilefilePath"], 'a' )
        self.logfilewriter=self.logfile.write
        self.allExisting[tablename]={}
        rowhead=', '.join(['\n','getAll',tablename,datetime.datetime.now().strftime('%Y%m%d%H%M%S')])
        allRecords = self.server.getAllRecords(tablename, ISTables.tables[tablename] )
        getAllWriter.writerows(allRecords)
        getAllWriterFile.close()
        returnVal=allRecords
        for eachresult in allRecords:
            self.allExisting[tablename][eachresult["Id"]]=eachresult
            rowText=[]
            for colName in eachresult.keys():
                pcol = ""
                pres=""
                if colName:
                    for eachChr in str(colName):
                        if ord(eachChr)<126:
                            pcol+=eachChr
                if eachresult[colName]:
                    for eachChr in str(eachresult[colName]):
                        if ord(eachChr)<126:
                            pres+=eachChr
                rowText+=[pcol, pres]
            self.logfilewriter(', '.join([rowhead, 'Retrieved', ''.join(rowText)]))
            # if tablename is 'Product':
            #     returnVal=allResults
            #     allResults.append(ISTableObjects.Product(eachresult))
        self.logfile.close()
        return returnVal

    def getProductTypeTables(self):
        returns={}
        productTables=["Product", "ProductCategory", "ProductCategoryAssign", ]
        for eachtable in productTables:
            returns[eachtable] = self.getAll(eachtable)
        return returns

    def __init__(self, server=None,appname=None,apikey=None):
        """
            Accepts either a server or log in credentials to create
            a server. From there creates variables 
                self.server=server 
                self.allExisting = dictionary to store all records
                known on the server. Dictionary will be formatted
                as 
                    self.allExisting[tablename][id]{dictionaryOfValues}
                for example the first part of a record may look like this:
                    self.allExisting['Product']['5']['BottomHTML']
                        should hold the data for the BottomHtml for product number 5
                If the items data structure is to be extended it should be by using
                nested dictionaries, like this:
                    self.allExisting['Product']['5']['categoryPaths']={}
                    self.allExisting['Product']['5']['categoryPaths']['awesome']={}
                    self.allExisting['Product']['5']['categoryPaths']['awesome']['actualPath']='awesome'
                    self.allExisting['Product']['5']['categoryPaths']['awesome']['parent']=None
                    self.allExisting['Product']['5']['categoryPaths']['awesome']['children']={}
                    self.allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']={}
                    self.allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['actualPath']='awesome/cool'
                    self.allExisting['Product']['5']['categoryPaths']['awesome']['parent']=self.allExisting['Product']['5']['categoryPaths']['awesome']
                etc.  Each object in the tree is either a 
                key:value pair, or a single object. this will 
                make traversing the tree a matter of 
                    traverseTree(TreeStructure):
                        retStr=""
                        for eachItem in TreeStructure.keys():
                            if type(TreeStructure[eachItem]) is type({}):
                                retStr += "\t"+eachItem + " : " + traverseTree(TreeStructure[eachItem])
                            else:
                                retStr += "\t" + eachItem + ":" + TreeStructure[eachItem] + "\n"
        """
        global ISServer
        global logFilePath
        self.server=server
        self.allExisting={}
        self.toAdd={}
        self.files={}
        timestamp=datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
        if 'logFilePath' in globals():
            self.folPath = logFilePath
        else:
            self.folPath = os.path.join(os.getcwd(), 'ISServer', self.server.infusionsoftapp, timestamp)
            logFilePath = self.folPath
        os.makedirs(self.folPath)
        self.files["logfilefilePath"]=os.path.join(self.folPath,"serverWorker.csv")
        self.logfile=open(self.files["logfilefilePath"], 'wb' )
        self.logfilewriter=self.logfile.write
        self.logfilewriter("\n" + "\t"*3 + "serverWorker\n" + timestamp + "\n" + os.path.realpath(__file__)+ "\n")
            # self.logfilewriter(os.path.realpath(__file__)+ " " + "ISServer")
        self.logfile.close()