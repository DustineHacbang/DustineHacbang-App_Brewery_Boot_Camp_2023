#######Dictionary######

Dictionary = "Will always have a key and a value"

#EXAMPLE#
#Bug and Function are the keys and the definition for each on is the values#
dictionary_example = {
    "KEY":"VALUE",
    "Bug":"An error in the prgoram preventing it from running",
    "Function": "A pice of code that can easily be called over and over again"
}

#Dictionary are useful due allow to group and tag information#

#HOW TO RETRIEVE ITEM FROM DICTIONARY#

#You will need to pass the "KEY" in "[]" with the name of the dictionary.
#IMPORTANT*** make sure it the key is in the correct data type
print(dictionary_example["KEY"])


#How to Add  a new item in the dictionary

#EXAMPLE
#in order to add a new item in the dictionary you need to call the dictionary and pass a new key in [].
#then to add the value you need to  "=" to a new value that it will be stored in
dictionary_example["Loop"] = "The action of doing somthing over and over again."

#Creating  an empty dictionary.
creating_new_dictionary = {}
#add items in new dictionary
creating_new_dictionary["NEW_KEY"] = "NEW VALUE"

#How to wipe a dictionary clean
creating_new_dictionary = {}

#How to edit an item in the dictionary
#pass in the key in the exiting dictionary and "=" to a new value
dictionary_example["Bug"] = "A moth in your computer"


#how to loop through a dictionary
for key in dictionary_example:
    #to gain access to the value in the dictionary you will need to set it up by
    #Name_Dictionary[Key] in order to gain the value
    print(dictionary_example[key])


#Nesting List and Dictionary#

sample_dictionary_list ={
    "key":["value","value2","value3"]
}

# Example
travel_log ={
    "France":{
        "Cities_Visted":["Paris", "Lille", "Dijon"],
        "total_visits": 12
        },
    "America":{
        "Cities_Visted":["Los Angeles","New York","Santa Cruz"],
        "total_visits": 20
    }
    }
###NESTED DICTIONARY#####
travel_log =[
    {
        "country":"France",
        "cities_Visted":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },

    {
        "country":"Germany",
        "cities_Visted":["Los Angeles","New York","Santa Cruz"],
        "total_visits": 20
    }
]