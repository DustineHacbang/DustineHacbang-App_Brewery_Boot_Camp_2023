# More Function with out put

# Example
def my_function(somthing):
    # do this
    # then this
    # finally do this
    pass

#Funtion with an output

def my_funtion():
    result = 3 * 2
    return result

output = my_function()

#Return will replaced where the fuction will be called 
# Meaning that my_function() will be come "result" once its done excuting equling to "output = result"

# Name Formater
#write a funtion that will use a return to format a name
#Example
def formant_name(f_name,l_name):
    cap_f_name = f_name.title()
    cap_l_name = l_name.title()
    full_name = cap_f_name + " " + cap_l_name
    return full_name

formated_string = formant_name("dustine","hacbang")
print(formated_string)

#"return marks the end of a function

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    cap_f_name = f_name.title()
    cap_l_name = l_name.title()
    full_name = cap_f_name + " " + cap_l_name
    return full_name

print(format_name(input("What is your first name?")))
