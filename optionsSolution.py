import xmlrpclib
import time
import random
import urllib
import base64
import csv
import productImage
import my_pw as pw
import infMon as iM
import re
############################################################
##  This is here as an example of what I was doing



# def sampleData(productsExport=pw.passwords['importFile']):
    # global server
    # global products
    # global productCatagories
    # blankProd=product("")
    # server = ISServer(appname, apikey)
    # thisProduct=None
    # with open(productsExport) as datas:
        # reader = csv.DictReader(datas)
        # for row in reader:
            # print str(row["Name"])
            # if (row["Name"] and row["Name"][0]=="["):
                # optionString=row["Name"]
                # optionString = optionString[4:].replace("\\,","_-_")
                # while(len(optionString)>0):
                    # if thisProduct.optionsSettings is None:
                        # thisProduct.optionsSettings={}
                    # optionType, optionString=optionString[1:3], optionString[4:]
                    # nextOptionStart=optionString.find('[')
                    # if (nextOptionStart>0):
                        # currentOptions,optionString = optionString[:nextOptionStart], optionString[nextOptionStart:]
                    # else:
                        # currentOptions,optionString=optionString,''
                    # try:
                        # theseOptions = currentOptions.split(',')
                    # except ValueError:
                        # theseOptions = [currentOptions,]
                    # for eachOption in theseOptions:
                        # print eachOption
                        # try:
                            # optionName,optionValue=eachOption.split("=")
                            # optionName = optionName.replace("_-_",",")
                        # except:
                            # optionName,optionValue=eachOption,"Whoops!"
                        # if optionName not in thisProduct.optionsSettings.keys():
                            # thisProduct.optionsSettings[optionName] = set()
                        # colonPlace=eachOption.find(':')
                        # if (colonPlace>0):
                            # eachOption = eachOption[:colonPlace]
                        # thisProduct.optionsSettings[optionName]=''.join(optionValue)
                # if (len(row["Price"])>0):
                    # priceOptionSeperator=row["Price"].find(']')
                    # priceChangeType, priceChange = row["Price"][:priceOptionSeperator].replace('[','').replace(']',''), row["Price"][priceOptionSeperator+1:]
                    # print str(thisProduct.id) + " ::: options " + priceChangeType + "  ::::" + priceChange
                    # if priceChangeType=="REMOVE":
                        # priceChange = str(-1*float(priceChange))
                    # optionChoice, optionChoiceValue = row["Name"][row["Name"].find(']')+1:].split("=",1)
                    # for eachS in [optionChoice, optionChoiceValue, priceChangeType, priceChange]:
                        # print eachS
                    # if thisProduct.optionsPriceChange is None:
                        # thisProduct.optionsPriceChange={}
                    # if optionChoice not in thisProduct.optionsPriceChange.keys():
                        # thisProduct.optionsPriceChange[optionChoice]={}
                    # thisProduct.optionsPriceChange[optionChoice][optionChoiceValue] = priceChange
            # else:
                # if thisProduct is not None:
                    # products.append(thisProduct)
                # thisProduct = product(row["Name"])
                # if (thisProduct.name=="" or thisProduct.name==None ):
                    # continue
                # for column in ["GPS Category", "Brand", "Category String"]:
                    # if (len(row[column])):
                        # thisProduct.catStrings.append(row[column].replace("\xe2\x84\xa2","TM"))
                # if row["SKU"]:
                    # thisProduct.sku = row["SKU"]
                # if row['Description']:
                    # thisProduct.description=row['Description']
                # if row["Price"]:
                    # thisProduct.price = row["Price"]
                # if row["Product Images"]:
                    # thisProduct.imageStrings.append(row["Product Images"])
                # if row["Meta Description"]:
                    # thisProduct.shortDescription = row["Meta Description"]
                # if row["Product Images"]:
                    # imageStrings=row["Product Images"].split("|")
                    # for eachS in imageStrings:
                        # for eachVal in eachS.split(","):
                            # if "Product Image URL: " in eachVal:
                                # thisProduct.images.append(eachVal.replace("Product Image URL: ","").strip())
                # thisProduct.id = server.cnp(thisProduct.prepare())
    # products.append(thisProduct)
    # for eachProduct in products:
        # if eachProduct.optionsSettings:
            # if eachProduct.options is None:
                # eachProduct.options = {}
            # counter=0
            # for eachOption in eachProduct.optionsSettings.keys():
                # counter+=1
                # thisOption = prodOption(eachProduct.id)
                # thisOption.name=eachOption
                # thisOption.label = eachOption
                # thisOption.required = 1
                # thisOption.order = counter
                # thisOption.optionType='FixedList'
                # thisOption.id = server.createNewRecord("ProductOption", thisOption.prepare())
                # eachProduct.options[eachOption] = thisOption
                # optionCounter=0
                # for eachValue in eachProduct.optionsSettings[eachOption]:
                    # optionCounter+=1
                    # newOptionValue=prodOptVal(thisOption.id)
                    # newOptionValue.optionIndex=optionCounter
                    # newOptionValue.label = eachValue
                    # newOptionValue.isdefault=0
                    # newOptionValue.name=eachValue
                    # if eachOption in eachProduct.optionsPriceChange.keys():
                        # if eachValue in eachProduct.optionsPriceChange[eachOption].keys():
                            # newOptionValue.adjustment=eachProduct.optionsPriceChange[eachOption][eachValue]
                    # newOptionValue.id = server.createNewRecord("ProductOptValue", newOptionValue.prepare())
                    # thisOption.values.append(newOptionValue)
        # print "prod ops complete"
        # for eachString in eachProduct.catStrings:
            # if eachProduct.categories is None:
                # eachProduct.categories={}
            # eachString.replace("\\/", "___")
            # for eachSubstring in eachString.split(";"):
                # thiscatid=getCatId(eachSubstring)
                # thisAssignment=prodCatAss(eachProduct.id, thiscatid)
                # thisAssignment.id=getCatAssiggnId(thisAssignment)
                # eachProduct.categories[eachSubstring]=eachProduct.categories[int(thiscatid)]=thisAssignment
    # return products


def sampleinputs():
    return [
"""[RB]Diameter=3"",[RB]Grit=800""",
"""[RB]Diameter=21"",[RB]Grit=1500""",
"""[RB]Diameter=24"",[RB]Grit=1500""",
"""[RB]Diameter=24""""",
"""[RB]Glass Weight=50 lb bag""",
"""[RB]Glass Weight=25 lb bag""",
"""[RB]Glass Weight=5 lb bag""",
"""[RB]Glass Weight=1 lb bag""",
"""[RB]Glass Weight=10 lb bag,[CS]Colors=Premium- Pineapple:2037.preview.jpg,Colors=Premium- Strawberry:2038.preview.jpg,Colors=Premium- Tangerine:2039.preview.jpg""",
"""[RB]Grit=16,[RT]Bond=Medium,[RB]Attachment Type=Polar Magnetic System""",
"""[RB]Grit=25,[RT]Bond=Medium,[RB]Attachment Type=Polar Magnetic System""",
"""[RB]Grit=40,[RT]Bond=Medium,[RB]Attachment Type=Polar Magnetic System""",
"""[RB]Grit=80,[RT]Bond=Medium,[RB]Attachment Type=Polar Magnetic System""",
"""[RB]Grit=150,[RT]Bond=Medium,[RB]Attachment Type=Polar Magnetic System""",
"""[RB]Grit=16,[RT]Bond=Medium,[RB]Attachment Type=Standard 3- Hole System"""
]

def parseOptions(optionString,currentProductOptions={}):
    numberOfOptionTypes=optionString.count('[')
    assert (numberOfOptionTypes>0 and len(optionString)>4)
    knownOptionTypes = ['RT', 'RB', 'CS']
    options={}
    for eachType in range(numberOfOptionTypes):
        optionType=optionString[1:3]
        print optionType
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
        for eachString in options[optionType]:
            eachString=eachString.strip(', ')
            for eachOptionDatum in re.split(r"[\[|,^\]]*",eachString):
                print eachOptionDatum
                if (len(eachOptionDatum)>0):
                    segmentedList=re.split(r"[,=:]",eachOptionDatum)
                    if segmentedList[0] not in currentProductOptions.keys():
                        currentProductOptions[segmentedList[0]]=set()
                    if (len(segmentedList)>1):
                        if segmentedList[0] not in currentProductOptions.keys():
                            currentProductOptions[segmentedList[0]]=set()
                        currentProductOptions[segmentedList[0]].add(segmentedList[1])
    return currentProductOptions

def parsePricing(optionString,currentProductOptions={}):
    """
    This function exists to accept a pricing string and return a 
    pricing dictionary with the intention of it being added directly
    to the products options variable.  
    ex: product.options={
        Glass Weight =set(50 lb bag, 10 lb bag, 1 lb bag, 25 lb bag, 5 lb bag)
        Diameter =set(3"" 24 24"" 21"")
        Grit set( 150 25 16 40 1500 80 800)
        Attachment Type set( Polar Magnetic System Standard 3- Hole System)
        Colors set( Premium- Pineapple Premium- Tangerine Premium- Strawberry)
        Bond set( Medium)
    }
    then set product.options["pricing"]

    """
    # this like this for testing
    currentProductOptions[optionString]=optionString
    return currentProductOptions

    #         if optionType not in optionsSorted.keys():
    #             optionsSorted[optionType]=[]
    #         optionsSorted[optionType]+=eachString.split(',')
    # return [options, optionsSorted]







# def testa():
#     thisProduct=iM.product('optionsHolder')
#     with open('optionsSample.csv') as datas:
#         reader = csv.DictReader(datas)
#         for row in reader:
#             if (row["Name"] and row["Name"][0]=="["):
#                 # Basically, if there is something in the "Name"
#                 # column, and it starts with '[', then it is
#                 # product option related
#                 optionString = row["Name"]

def testfunction():
    resultsHolder={}
    for eachTest in sampleinputs():
        resultsHolder=parseOptions(eachTest,resultsHolder)
    return resultsHolder