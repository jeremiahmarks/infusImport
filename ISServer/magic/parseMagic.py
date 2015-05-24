#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-23 19:09:58
# @Last Modified 2015-05-23
# @Last Modified time: 2015-05-23 23:23:31

import re
import string
import csv
import uglyObjects
import sqlalchemy

global products
global productCatagories

if 'products' not in globals():
    products={}
if 'productCatagories' not in globals():
    productCatagories={}



class uglyStyle(object):

    def getRowType(self, row):
        self.checkAndSyncGlobals()
        if len(row["Name"]) is 0:
            return "skuPricing"
        elif (row["Name"][0] is not "["):
            return "product"
        elif (len(row["SKU"])==0):
            return "pricingRule"
        else:
            return "option"

    def parseProductRow(self,productRow):
        global products
        thisProduct = uglyObjects.product(productRow["Name"])
        thisProduct.optionsTree={}
        thisProduct.options={}
        if 'products' not in globals():
            products={}
        products[thisProduct.ProductName]=thisProduct
        for column in ["GPS Category", "Brand", "Category String"]:
            if (len(productRow[column])):
                data=""
                for eachChar in productRow[column]:
                    if ord(eachChar)<=126:
                        data+=eachChar
                thisProduct.catStrings[column]=data
        if productRow["SKU"]:
            thisProduct.sku = productRow["SKU"]
        if productRow['Description']:
            thisProduct.description=productRow['Description']
        if productRow["Price"]:
            thisProduct.price = productRow["Price"]
        if productRow["Product Images"]:
            thisProduct.imageStrings["Product Images"]=productRow["Product Images"]
        if productRow["Meta Description"]:
            thisProduct.shortDescription = productRow["Meta Description"]
        if productRow["Product Images"]:
            imageStrings=productRow["Product Images"].split("|")
            for eachS in imageStrings:
                for counter, eachVal in enumerate(eachS.split(",")):
                    if "Product Image URL: " in eachVal:
                        thisProduct.images[counter]=eachVal.replace("Product Image URL: ","").strip()
        return thisProduct

    def parseSkuRow(self,skuRow,currentProductOptions={}):
        self.checkAndSyncGlobals()
        optionString=skuRow["Name"]
        sku=skuRow["SKU"]
        pricing=skuRow["Price"]
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
            if optionType is not "skuPricing":
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
                                if segmentedList[0] not in knownOptionTypes:
                                    if segmentedList[0] not in currentProductOptions.keys():
                                        currentProductOptions[segmentedList[0]]={'skud': {} }
                                    if segmentedList[0] not in currentProductOptions[segmentedList[0]]['skud'].keys():
                                        currentProductOptions[segmentedList[0]]['skud'][segmentedList[0]]=sku
                            if priceChange is not None:
                                if segmentedList[0] not in knownOptionTypes:
                                    currentProductOptions[segmentedList[0]]['pricing'][segmentedList[1]]=priceChange
        return currentProductOptions

    def parsePricingRow(self,pricingRow,currentProductOptions={}):
        return self.parseSkuRow(pricingRow,currentProductOptions={})

    def parseOptionRow(self,optionRow,currentProductOptions={}):
        return self.parseSkuRow(optionRow,currentProductOptions={})

    def checkAndSyncGlobals(self):
        if 'products' not in globals():
            self.products={}
            products=self.products
        else:
            self.products=products

        if products is not self.products
            self.products=products

        if 'productCatagories' not in globals():
            self.productCatagories={}
            productCatagories=self.productCatagories
        else:
            self.productCatagories=productCatagories

        if productCatagories is not self.productCatagories
            self.products=products
