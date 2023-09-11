"""
DICKionaries

Builtin Methods:
    dict.get()
    dict.pop()
    dict.values()
    dict.keys()
    dict.items()
    dict.update()

Objectives:
    -Go over builtin methods
    -Understand how to iterate over dictionaries
    -Comparing dictionaries
    -Memory allocation and deepcopy()
"""


def getTesting(someDict):
    # billy = someDict['billy']
    billy = someDict.get('billys').get('age')
    print(f"billy equals: {billy}")
    
    # more code below
    # for something in billy:
    #     pass

def popTesting(someDict):
    mandy = someDict.pop('mandy', {}).pop('age')
    print('Mandy Variable', mandy)
    print('Entire Dict', someDict)

def keysTesting(someDict):
    for key in someDict.keys():
        print(key)
    

def valuesTesting(someDict):
    print(someDict.values())
    # for value in someDict.values():
    #     print(value)

def itemsTesting(someDict):
    for key, value in someDict.items():
        print('key is: ', key)
        print('value is: ', value)

def updateTesting(someDict):
    newDict = {
        'billy':  {
            'age': 55,
            'gender': "F"
        },
    }
    someDict.update(newDict)
    print(someDict)

myDict = {
    'mandy': {
        'age': 55,
        'gender': "F"
    },
    'billy': {
        'age': 43,
        'gender': 'M'
    }
}
from copy import deepcopy

def modifyDict(myDict):
    myDict[1] = "monkey"
    # myDict['testVar1'] = 1
    # brandNewVar = deepcopy(myDict)
    # brandNewVar['test'] = 1
    # otherVar = brandNewVar
    # myDict['testVar2'] = 10
    # otherVar['testVar3'] = 11

myList = ["jasonisamonkey", "chinchin"]
modifyDict(myList)
print(myList)



# 
# getTesting(myDict)
# popTesting(myDict)
# keysTesting(myDict)
# valuesTesting(myDict)
# itemsTesting(myDict)
# updateTesting(myDict)