#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-16 14:44:14
# @Last Modified 2015-05-19
# @Last Modified time: 2015-05-19 21:07:10
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
        vals["ProductName"]=self.name
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



if 'products' not in globals():
    print "Products now exist as an empty set"
    products=[]

def pr(something):
    print something

def toFile(something):
    global logFile
    if 'logFile' not in globals():
        logfile={}
        logfile['filename']='ISProduct_log_file.md'
        logfile['writer']=open(logfile['filename'],'a')
    logfile['writer'].write(something)

def printrowsandpermissions(method=pr):
  justVar=35
  fieldStr=""
  typeStr=""
  edStr=""
  addStr=""
  redStr=""
  delStr=""
  for eachRow in Product.keys():
    fieldStr = fieldStr + eachRow.ljust(justVar)

    if ("Edit" in Product[eachRow]["permissions"]):
      edStr=edStr + "Edit".ljust(justVar)
    else:
      edStr = ''.ljust(justVar)

    if ("Add" in Product[eachRow]["permissions"]):
      addStr=addStr + "Add" .ljust(justVar)
    else:
      addStr = ''.ljust(justVar)

    if ("Read" in Product[eachRow]["permissions"]):
      redStr=redStr + "Read".ljust(justVar)
    else:
      redStr = ''.ljust(justVar)

    if ("Delete" in Product[eachRow]["permissions"]):
      delStr=delStr + "Delete".ljust(justVar)
    else:
      delStr = ''.ljust(justVar)

  method(fieldStr)
  method(typeStr)
  method(edStr)
  method(addStr)
  method(redStr)
  method(delStr)

