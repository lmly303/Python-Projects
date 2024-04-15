def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter == " ":
            cipher_text += " "
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 26:
                new_position = new_position - 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")


def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter == " ":
            cipher_text += " "
        else:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            if new_position < 0:
                new_position = 26 + new_position
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x="yes"
while x=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(plain_text=text, shift_amount=shift)

    x=input("type 'yes' to continue and 'no' to terminate : ")





