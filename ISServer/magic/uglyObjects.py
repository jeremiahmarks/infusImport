#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-23 19:16:33
# @Last Modified 2015-05-23
# @Last Modified time: 2015-05-23 19:27:34
global products
global productCatagories

class product(object):

    def __init__(self, name):
        self.id=None
        self.ProductName=name
        self.categories=None
        self.catStrings={}
        self.sku=None
        self.description=None
        self.price=0.00
        self.isActive=1
        self.images={}
        self.imageStrings={}
        self.shortDescription=None
        self.taxable=-1
        self.cityTax=-1
        self.countryTax=-1
        self.stateTax=-1
        self.shippable=-1
        self.weight=None
        self.options=None
        self.optionsSettings=None
        self.optionsPriceChange={}
        ##self.

    def prepare(self):
        vals={}
        vals["ProductName"]=self.ProductName
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
        self.children={}
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
        self.values={}

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