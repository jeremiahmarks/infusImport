#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-16 14:44:14
# @Last Modified 2015-05-19
# @Last Modified time: 2015-05-19 23:20:41
global products

ProductTable = {
"BottomHTML":           {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"CityTaxable":          {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"CountryTaxable":       {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"Description":          {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"HideInStore":          {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"Id":                   {"type": "Id",      'permissions' : [ "Read", ] },
"InventoryLimit":       {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"InventoryNotifiee":    {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"IsPackage":            {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"LargeImage":           {"type": "Blob",    'permissions' : [ "Edit", "Add", "Read", ] },
"NeedsDigitalDelivery": {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"ProductName":          {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"ProductPrice":         {"type": "Double",  'permissions' : [ "Edit", "Add", "Read", ] },
"Shippable":            {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"ShippingTime":         {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"ShortDescription":     {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"Sku":                  {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"StateTaxable":         {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"Status":               {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"Taxable":              {"type": "Integer", 'permissions' : [ "Edit", "Add", "Read", ] },
"TopHTML":              {"type": "String",  'permissions' : [ "Edit", "Add", "Read", ] },
"Weight":               {"type": "Double",  'permissions' : [ "Edit", "Add", "Read", ] }
}

class product(object):

    def __init__(self, values):

        if 'products' not in globals():
            print "Products now exist as an empty set"
            products=[]

        if ("BottomHTML" in values.keys()):
            self.BottomHTML = options["BottomHTML"]#String
        else:
            self.BottomHTML=None

        if ("CityTaxable" in values.keys()):
            self.CityTaxable = options["CityTaxable"]#Integer
        else:
            self.CityTaxable=None

        if ("CountryTaxable" in values.keys()):
            self.CountryTaxable = options["CountryTaxable"]#Integer
        else:
            self.CountryTaxable=None

        if ("Description" in values.keys()):
            self.Description = options["Description"]#String
        else:
            self.Description=None

        if ("HideInStore" in values.keys()):
            self.HideInStore = options["HideInStore"]#Integer
        else:
            self.HideInStore=None

        if ("Id" in values.keys()):
            self.Id = options["Id"]#Id
        else:
            self.Id=None

        if ("InventoryLimit" in values.keys()):
            self.InventoryLimit = options["InventoryLimit"]#Integer
        else:
            self.InventoryLimit=None

        if ("InventoryNotifiee" in values.keys()):
            self.InventoryNotifiee = options["InventoryNotifiee"]#String
        else:
            self.InventoryNotifiee=None

        if ("IsPackage" in values.keys()):
            self.IsPackage = options["IsPackage"]#Integer
        else:
            self.IsPackage=None

        if ("LargeImage" in values.keys()):
            self.LargeImage = options["LargeImage"]#Blob
        else:
            self.LargeImage=None

        if ("NeedsDigitalDelivery" in values.keys()):
            self.NeedsDigitalDelivery = options["NeedsDigitalDelivery"]#Integer
        else:
            self.NeedsDigitalDelivery=None

        if ("ProductName" in values.keys()):
            self.ProductName = options["ProductName"]#String
        else:
            self.ProductName=None

        if ("ProductPrice" in values.keys()):
            self.ProductPrice = options["ProductPrice"]#Double
        else:
            self.ProductPrice=None

        if ("Shippable" in values.keys()):
            self.Shippable = options["Shippable"]#Integer
        else:
            self.Shippable=None

        if ("ShippingTime" in values.keys()):
            self.ShippingTime = options["ShippingTime"]#String
        else:
            self.ShippingTime=None

        if ("ShortDescription" in values.keys()):
            self.ShortDescription = options["ShortDescription"]#String
        else:
            self.ShortDescription=None

        if ("Sku" in values.keys()):
            self.Sku = options["Sku"]#String
        else:
            self.Sku=None

        if ("StateTaxable" in values.keys()):
            self.StateTaxable = options["StateTaxable"]#Integer
        else:
            self.StateTaxable=None

        if ("Status" in values.keys()):
            self.Status = options["Status"]#Integer
        else:
            self.Status=None

        if ("Taxable" in values.keys()):
            self.Taxable = options["Taxable"]#Integer
        else:
            self.Taxable=None

        if ("TopHTML" in values.keys()):
            self.TopHTML = options["TopHTML"]#String
        else:
            self.TopHTML=None

        if ("Weight" in values.keys()):
            self.Weight = options["Weight"]#Double
        else:
            self.Weight=None

        self.categories=None
        self.catStrings=[]
        self.images=[]
        self.imageStrings=[]
        self.options=None
        self.optionsSettings=None
        self.optionsPriceChange={}



    def prepare(self):
        vals={}
        if self.BottomHTML is not None:
            vals["BottomHTML"] = self.BottomHTML =#        if (self.sku):
        if self.CityTaxable is not None:
            vals["CityTaxable"] = self.CityTaxable   =#            vals["Sku"] = self.sku
        if self.CountryTaxable is not None:
            vals["CountryTaxable"] = self.CountryTaxable =#        if (self.description):
        if self.Description is not None:
            vals["Description"] = self.Description   =#            vals["Description"] = self.description
        if self.HideInStore is not None:
            vals["HideInStore"] = self.HideInStore   =#        vals["ProductPrice"] = self.price
        if self.Id is not None:
            vals["Id"] = self.Id =#        if (self.isActive>=0):
        if self.InventoryLimit is not None:
            vals["InventoryLimit"] = self.InventoryLimit =#            vals["Status"] = self.isActive
        if self.InventoryNotifiee is not None:
            vals["InventoryNotifiee"] = self.InventoryNotifiee   =#        if (self.shortDescription):
        if self.IsPackage is not None:
            vals["IsPackage"] = self.IsPackage   =#            vals["ShortDescription"]=self.shortDescription
        if self.LargeImage is not None:
            vals["LargeImage"] = self.LargeImage =#        if (self.taxable>=0):
        if self.NeedsDigitalDelivery is not None:
            vals["NeedsDigitalDelivery"] = self.NeedsDigitalDelivery =#            vals["Taxable"]=self.taxable
        if self.ProductName is not None:
            vals["ProductName"] = self.ProductName   =#        if (self.cityTax>=0):
        if self.ProductPrice is not None:
            vals["ProductPrice"] = self.ProductPrice =#            vals["CityTax"]=self.cityTax
        if self.Shippable is not None:
            vals["Shippable"] = self.Shippable   =#        if (self.stateTax>=0):
        if self.ShippingTime is not None:
            vals["ShippingTime"] = self.ShippingTime =#            vals["StateTax"] = self.stateTax
        if self.ShortDescription is not None:
            vals["ShortDescription"] = self.ShortDescription =#        if (self.countryTax>=0):
        if self.Sku is not None:
            vals["Sku"] = self.Sku   =#            vals["CountryTax"] = self.countryTax
        if self.StateTaxable is not None:
            vals["StateTaxable"] = self.StateTaxable =#        if (self.shippable>=0):
        if self.Status is not None:
            vals["Status"] = self.Status =#            vals["Shippable"] = self.shippable
        if self.Taxable is not None:
            vals["Taxable"] = self.Taxable   =#        if (self.weight):
        if self.TopHTML is not None:
            vals["TopHTML"] = self.TopHTML   =#            vals["Weight"] = self.weight
        if self.Weight is not None:
            vals["Weight"] = self.Weight =#        return vals
        return vals

    def setAppName(self, appname):
        self.appname=appname

    def setServer(self,parentServer):
        self.server=parentServer
        self.appname=server.infusionsoftapp

    def getPublicPage(self, appname):
        if self.id is not None:
            return "https://" + server.infusionsoftapp + ".infusionsoft.com/app/storeFront/showProductDetail?productId=" + str(self.Id)
        else:
            return "I do not seem to have an ID."

    def getInternalPage(self):
        if self.id is not None:
            return "https://" + server.infusionsoftapp + ".infusionsoft.com/app/product/manageProduct?productId=" + str(self.Id)
        else:
            return "I do not seem to have an ID."

    def detailedData(self):

        externalValues={}
        externalValues['publicPage'] = self.getPublicPage()
        externalValues['internalPage'] = self.getInternalPage()
        externalValues.update(self.vals())
        return externalValues





