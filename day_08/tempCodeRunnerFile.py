 cipher_text = ""
    for letter in original_text:
        shifted_position = alphabets.index(letter) + shift_amount #7 + 2 
        cipher_text += alphabets[shifted_position]