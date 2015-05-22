import re

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
#  "%090i"%(int(c))
# '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000150'
def parseOptions(optionString,currentProductOptions={}):
    numberOfOptionTypes=optionString.count('[')
    assert (numberOfOptionTypes>0 and len(optionString)>4)
    knownOptionTypes = ['RT', 'RB', 'CS']
    options={}
    for eachType in range(numberOfOptionTypes):
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
        for eachString in options[optionType]:
            eachString=eachString.strip(', ')
            for eachOptionDatum in re.split(r"[\[|,^\]]*",eachString):
                # print eachOptionDatum
                if (len(eachOptionDatum)>0):
                    segmentedList=re.split(r"[,=:]",eachOptionDatum)
                    if (len(segmentedList)>1):
                        if segmentedList[0] not in currentProductOptions.keys():
                            currentProductOptions[segmentedList[0]]={'pricing':{}, 'options': set()}
                        currentProductOptions[segmentedList[0]]['options'].add(segmentedList[1])
    return currentProductOptions

def sampleOptions():
    holder={}
    for option in sampleinputs():
        holder=parseOptions(option,holder)
    return holder