#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-22 20:18:37
# @Last Modified 2015-05-23
# @Last Modified time: 2015-05-23 18:18:17
import my_pw
import ISServer
import serverFunctions

def testone():
    thisServer=ISServer.ISServer(my_pw.passwords['appname'],my_pw.passwords['apikey'])
    myWorker=serverFunctions.serverWorker(thisServer)
    return myWorker.getAll("Product")

def fillProductTables(myWorker):
    myWorker.getProductTypeTables()
    return myWorker

def getWorker():
    thisServer=ISServer.ISServer(my_pw.passwords['appname'],my_pw.passwords['apikey'])
    myWorker=serverFunctions.serverWorker(thisServer)
    return myWorker

def delProdCat(myWorker):
    myWorker.delAll('ProductCategory')

def main():
    myWorker=getWorker()
    myWorker.getProductTypeTables()
