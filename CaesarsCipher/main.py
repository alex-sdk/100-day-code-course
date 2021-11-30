from art import logo


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    index = -1
    for letter in plain_text:
        if letter in alphabet:
            for letters in alphabet:
                index += 1
                if letter == letters:
                    cipher_text += alphabet[index + shift_amount]
                    index = -1
                    break
        else:
            cipher_text += letter
    print(f"Here is the cipher: {cipher_text}.")


def decrypt(cipher, shift_amount):
    plaintxt = ""
    index = -1
    for letter in cipher:
        for letters in alphabet:
            index += 1
            if letter == letters:
                plaintxt += alphabet[index - shift_amount]
                index = -1
                break
    print(f"Here is the decoded word: {plaintxt}.")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
gamestatus = True
while gamestatus:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # catch index errors
    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
        gamestatus = False
    elif direction == "decode":
        decrypt(cipher=text, shift_amount=shift)
        gamestatus = False
    else:
        print("Please enter valid input")

    if gamestatus == False:
        restart = input(
            "Type 'Yes' to restart the program and decode your word. Otherwise type no.\n")
        if restart.lower() == "yes":
            gamestatus = True
            print(logo)
