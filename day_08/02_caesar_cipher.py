from art import logo

print(logo)
print("Welcome to the Caesar Cipher")
print("=" * 50)

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabets:  #  Check if individual LETTER is in alphabets
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
        else:
            output_text += letter  # ✅ Keep non-alphabetic characters (spaces, punctuation)
    
    print(f"The {encode_or_decode}d text is: {output_text}")

# Main program loop
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: "))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Type 'yes' if you want to go again, otherwise type 'no': \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


#alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#            0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
# print(alphabets.index("a"))  # Output: 0
# print(alphabets.index("h"))  # Output: 7  
# print(alphabets.index("z"))  # Output: 25


# def encrypt(original_text , shift_amount):
#     cipher _text = ""
#     for letter in original_text:
#         shifted_position = alphabets.index(letter) + shift_amount #7 + 2 
#         shifted_position %= len(alphabets)#division algorithm rule has ascendant 
#         cipher_text += alphabets[shifted_position]
 
#     print(f"the encrypt code is {cipher_text}")

# encrypt(original_text =  text , shift_amount = shift)    

# def decrypt(original_text , shift_amount):
#     decipher_text = ""
#     for letter in original_text:
#         shifted_position =alphabets.index(letter) - shift_amount
#         shifted_position %= len(alphabets)
#         decipher_text += alphabets[shifted_position]
#     print(f"the decrypt code is {decipher_text}")

# decrypt(original_text=text , shift_amount=shift)