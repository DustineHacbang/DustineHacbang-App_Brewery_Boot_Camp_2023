#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(normal_text,shift_amount):  
    encrypted_text = ""
    #itterate through the normal_text letter by letter
    for letter in normal_text:
        #finds the index of the letter in normal_text from alpahbet list
        position = alphabet.index(letter)
        #find the shifted value from the alpahbet list
        new_position = position + shift_amount
        #fixes the bug that out of bound index error and resetting the     
        #counter to the begining of the list of alpahbet
    if new_position > alphabet.index("z"):
        reset_shift_num = alphabet.index("z") - position
        new_position = (shift_amount - reset_shift_num) - 1
    #putting the new letters into a string so it may be printed
    new_letter = alphabet[new_position]
    encrypted_text += new_letter
    
    encrypt(normal_text,shift_amount * -1)
    print(f"The encoded text is {encrypted_text}")
    
encrypt(normal_text=text, shift_amount=shift)
