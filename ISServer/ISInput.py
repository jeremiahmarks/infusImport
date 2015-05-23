#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-19 23:29:21
# @Last Modified 2015-05-20
# @Last Modified time: 2015-05-20 01:15:35
############################################################
## This module exists to take data from a CSV file and attempt
## to turn it into datastructure objects.

import csv
from my_pw import passwords
############################################################
# These are my different data structures.
from ISTableObjects import Product, ProductCategory, ProductCategoryAssign, ProductInterest, ProductInterestBundle, ProductOptValue, ProductOption
############################################################
# 



def parseInput():
    global products
    thisProduct=None
    filestyle=None
    with open(productsExport) as datas:
        reader = csv.DictReader(datas)
        parser=Parser()
        for row in reader:
            rowtype=parser.getRowType(row)
            if (rowtype=='product'):
                if thisProduct is not None:
                    #put the last one away so we can build the 
                    #new one.
                    products.append(thisProduct)
                thisProduct=Product(row)
            if (rowtype=='options'):
                pass
            if (rowtype=='pricing'):
                pass



class filecleaner(object):
    def  cleanHeadinglessColumns(infile, outfile):
        """
        This will remove data in columns without headings
        """
        rawData=open(filename,'rb')
        reader=csv.DictReader(rawData)
        outfile='prodOut.csv'
        cleanedData=open(outfile,'wb')
        writer=csv.DictWriter(cleanedData,reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if None in row.keys():
                row.pop(None,None)
            writer.writerow(row)
        cleanedData.close()
        rawData.close()



class fileStyle(object):
    """
    This is a base class to build input formats off of. 
    """
    global products
    global productcategorys
    global productcategoryassigns
    global productinterests
    global productinterestbundles
    global productoptvalues
    global productoptions

class Parser(object):
    global products
    global productcategorys
    global productcategoryassigns
    global productinterests
    global productinterestbundles
    global productoptvalues
    global productoptions

    """
    This class exists to handle different formats of csv files
    """
    def __init__(self):
        self.backupFile=None
        return self

    def process(self, row):
        rowtype=self.getRowType(row)
        if (rowtype=='product'):



    def getRowType(self, row):
        if not(len(row['Name'])>0):
            #this would be a product bundle type option.
            #for now I cannot figure out a good way to do this
            #so I am skipping them
            continue
        if (row['Name'][0]=="["):
            #this indicates that this row is a not a product
            if (len(row['Price'])>0):
                #this indicates that this is a pricing rule
                return 'pricing'
            else:
                #len(row['Price']==0)
                #The fact that it did have a "[" in the first
                #character indicates that it is not a product
                #The fact that it does not have anything in
                #the price column indicates that it is an
                #option
                return "options"
        else:
            return "product"





        if row['SKU'] is not None:
            self.processthis
        if row['Allow Purchases'] is not None:
            self.processthis
        if row['Product Condition'] is not None:
            self.processthis
        if row['GPS Enabled'] is not None:
            self.processthis
        if row['GPS Manufacturer Part Number'] is not None:
            self.processthis
        if row['Meta Description'] is not None:
            self.processthis
        if row['Category Details'] is not None:
            self.processthis
        if row['Product URL'] is not None:
            self.processthis
        if row['Brand'] is not None:
            self.processthis
        if row['Product Availability'] is not None:
            self.processthis
        if row['Product Images'] is not None:
            self.processthis
        if row['GPS Category'] is not None:
            self.processthis
        if row['Category String'] is not None:
            self.processthis
        if row['Product Files'] is not None:
            self.processthis
        if row['Option Set'] is not None:
            self.processthis
        if row['Description'] is not None:
            self.processthis
        if row['\xef\xbb\xbfNameID'] is not None:
            self.processthis
        if row['Price'] is not None:
            self.processthis
        if row['Name'] is not None:
            self.processthis