#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-22 20:20:29
# @Last Modified 2015-05-23
# @Last Modified time: 2015-05-23 03:08:38


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
        rowhead=', '.join(['\n','delAll',tablename,datetime.datetime.now().strftime('%Y%m%d%H%M%S')])
        if tablename not in ISTableObjects.deletableTables:
            self.logfilewriter(', '.join([rowhead,"I cannot delete from that table"]))
            return False
        allRecords = self.server.getAllRecords(tablename, ISTables.tables[tablename] )
        for eachresult in allRecords:
            rowText=[]
            for colName in eachresult.keys():
                rowText+=[colName, eachresult[colName]]
            self.server.deleteRecord(tableName, eachresult['Id'])
            self.logfilewriter(', '.join([rowhead, 'deleted', rowText]))

    def getAll(self, tablename):
        """
        getAll accepts a table name and will return all values
        from that table. It will return them in a list of dictionaries.
        """
        getAlltimestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        getAllWriterFile=open(os.path.dirname(self.logfilefilePath)+"getAll"+getAlltimestamp,'wb')
        getAllWriter=csv.DictWriter(getAllWriterFile, ISTables.tables[tablename], delimiter=',')
        getAllWriter.writeheader()
        self.logfile=open(self.logfilefilePath, 'a' )
        self.logfilewriter=self.logfile.write
        rowhead=', '.join(['\n','getAll',tablename,datetime.datetime.now().strftime('%Y%m%d%H%M%S')])
        allRecords = self.server.getAllRecords(tablename, ISTables.tables[tablename] )
        allResults=[]
        getAllWriter.writerows(allRecords)
        getAllWriterFile.close()
        returnVal=allRecords
        for eachresult in allRecords:
            rowText=[]
            for colName in eachresult.keys():
                rowText+=[colName, eachresult[colName]]
            self.logfilewriter(', '.join([rowhead, 'Retrieved', ''.join(''.join(str([rowText])))]))
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

    def __init__(self, server=None):
        global ISServer
        global logfilewriter
        self.server=server
        if 'ISServer' in globals():
            folPath = os.path.dirname(ISServer.__file__)
        else:
            folPath = os.getcwd()
        timestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        folPath = os.path.join(folPath, timestamp)
        os.makedirs(folPath)
        self.logfilefilePath=os.path.join(folPath,"serverWorker"+timestamp)
        self.logfile=open(self.logfilefilePath, 'wb' )
        if 'logfilewriter' not in globals():
            self.logfilewriter=self.logfile.write
            logfilewriter = self.logfilewriter
            self.logfilewriter(os.path.realpath(__file__)+ " " + "\nI should probably be the main directory of this thing\n")
        else:
            self.logfilewriter = logfilewriter
            # self.logfilewriter(os.path.realpath(__file__)+ " " + "ISServer")
        self.logfile.close()