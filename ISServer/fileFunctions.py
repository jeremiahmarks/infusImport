#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-23 18:35:04
# @Last Modified 2015-05-24
# @Last Modified time: 2015-05-24 02:24:32
import os
import my_pw
import datetime
import csv
import magic
from magic import parseMagic
import sqlalchemy

global logFilePath
global products
global productCatagories

if 'products' not in globals():
    products={}
if 'productCatagories' not in globals():
    productCatagories={}

class fileWorker(object):
    def __init__(self,csvFile=None,server=None,appName=None):
        global logFilePath
        timestamp=datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
        self.files={}
        self.server=server
        self.appName=appName
        if csvFile is None:
            self.files['originalCSV']=my_pw.passwords['importFile']
        else:
            self.files['originalCSV']=csvFile
        if self.server is not None:
            self.appName = server.infusionsoftapp
        if 'logFilePath' in globals():
            self.folPath = logFilePath
        else:
            if self.appName is not None:
                self.folPath = os.path.join(os.getcwd(), 'ISServer', self.appName, 'folderWorker', timestamp)
            else:
                self.folPath = os.path.join(os.getcwd(), 'ISServer', 'folderWorker', timestamp)
            logFilePath = self.folPath
        os.makedirs(self.folPath)
        basedir=os.path.abspath(self.folPath)
        sqlpath='''sqlite:////'''+os.path.join(basedir, timestamp +"test.sqlite")
        self.files["logfilefilePath"]=os.path.join(self.folPath,"fileWorker.csv")
        self.logfile=open(self.files["logfilefilePath"], 'wb' )
        self.logfilewriter=self.logfile.write
        self.logfilewriter("\n" + "\t"*3 + "fileWorker\n" + timestamp + "\n" + os.path.realpath(__file__)+ "\n")
            # self.logfilewriter(os.path.realpath(__file__)+ " " + "ISServer")
        self.logfile.close()

    def parseCSV(self):
        parser=parseMagic.uglyStyle()
        rowHolder={}
        self.files["parsed"]={}
        reader=csv.DictReader(open(self.files['originalCSV'], 'rb'))
        for rownum, row in enumerate(reader):
            rowType=parser.getRowType(row)
            if rowType not in rowHolder.keys():
                rowHolder[rowType]={}
            rowHolder[rowType][rownum]=row

            if rowType=="product":
                thisProduct=parser.parseProductRow(row)

            if rowType=="skuPricing":
                thisSku=parser.parseSkuRow(row,thisProduct.options)

            if rowType=="pricingRule":
                thisPricing=parser.parsePricingRow(row, thisProduct.options)

            if rowType=="option":
                thisOption=parser.parseOptionRow(row, thisProduct.options)

        if rowHolder:
            for eachType in rowHolder.keys():
                if eachType not in self.files["parsed"].keys():
                    self.files["parsed"][eachType]=''
                if len(rowHolder[eachType])>0:
                    timestamp=datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
                    self.files["parsed"][eachType]=os.path.join(self.folPath, eachType+".csv")
                    headers=rowHolder[eachType][rowHolder[eachType].keys()[0]].keys()
                    print headers
                    quickWriterFile=open(self.files["parsed"][eachType], 'wb+')
                    quickWriter=csv.DictWriter(quickWriterFile,['rowNumber'] + headers)
                    print quickWriter.fieldnames
                    quickWriter.writeheader()
                    for eachRowNum in rowHolder[eachType].keys():
                        rowHolder[eachType][eachRowNum]['rowNumber']=eachRowNum
                        print rowHolder[eachType][eachRowNum]
                        quickWriter.writerow(rowHolder[eachType][eachRowNum])
                    quickWriterFile.close()
        return rowHolder

