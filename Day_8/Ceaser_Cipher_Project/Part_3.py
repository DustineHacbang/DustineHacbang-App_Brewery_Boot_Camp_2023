alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceaser(start_text, shift_amount, direction_type):
    converted_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if direction_type == "encode":
            new_position = position + shift_amount
        elif direction_type == "decode":
            new_position = position - shift_amount
        converted_text += alphabet[new_position]
    print(f"The {direction_type} text is {converted_text}")


ceaser(start_text=text, shift_amount=shift, direction_type=direction)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.