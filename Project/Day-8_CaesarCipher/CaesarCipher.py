from logo import logo

print(logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shouldContinue = False


def cipher(text, shift, direction):
    cipherTest = ""
    if direction == "decode":
        shift = shift * -1

    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            newPosition = position + shift
            cipherTest += alphabets[newPosition]
        else:
            cipherTest += letter

    print (f"Here\'s the {direction}ed text : {cipherTest}")


while not shouldContinue:
    userInput = input("Type \'encode\' to encrypt, type \'decode\' to decrypt: \n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    cipher(message, shift, userInput)

    again = input ("Type \'yes\' if you want to go again. otherwise type \'no\' : ")
    if again == "no":
        shouldContinue = True

