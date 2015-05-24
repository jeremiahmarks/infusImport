#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-23 23:06:08
# @Last Modified 2015-05-24
# @Last Modified time: 2015-05-24 02:47:17
import csv
import sqlalchemy
import my_pw
import ISServer
import os
import ISTables
global products
global productCatagories




class CsvDatabase(object):
    def __init__(self): #, csvFile, appname=my_pw.passwords['appname']):
        self.startStamp=ISServer.ISServer.timeStamp()
        self.basedir=os.path.join(os.path.dirname(os.path.abspath(ISServer.__file__)), "csvDatabase",self.startStamp)
        os.makedirs(self.basedir)
        self.sqlpath='''sqlite://///home/jlmarks/infusImport/ISServer/csvDatabase/DEV.sqlite'''
        print self.sqlpath
        self.db=sqlalchemy.create_engine(self.sqlpath)
        self.dbConnection=self.db.connect()
        self.dbCursor=self.dbConnection.connection.cursor()

    def createTable(self,tableName, columnData):
        creationString="CREATE TABLE " + tableName + "\n("
        for eachColumnName in columnData.keys():
            creationString += eachColumnName + " " + columnData[eachColumnName]+ ", "
        creationString=creationString[:-2]+")"
        print creationString
        self.dbCursor.execute(creationString)
        self.commitTodb()
    def addValuesToTable(self, tableName,values):
        additionString="INSERT INTO " + tableName + " VALUES(" + values + ")"
        print additionString
        self.dbCursor.execute(additionString)
        self.commitTodb()

    def commitTodb(self):
        self.dbCursor.commit()

    def closeConn(self):
        self.dbConnection.close()

def example():
    db=CsvDatabase()
    tname="Products"
    tvals={}
    tvals['Id']="INTEGER PRIMARY KEY ASC"
    tvals['ProductName']="varchar(250) NOT NULL"
    db.createTable(tname, tvals)





# a=CsvDatabase()
# b=a.db.connect()
# c=b.connection.cursor()
# c
# c.execute('''
# Create table ProductsFromFile(rownumber INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
# ''')
