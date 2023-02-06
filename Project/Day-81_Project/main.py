import pandas

code_morse = {}
with open("test.txt","r",encoding="utf-8") as my_data:
    # data = my_data.read()
    for line in my_data:
        k,v = line.split()
        code_morse[k] = v


user_input = input("Input message to translate to code morse: ")
text=""
for messages in user_input:
    text += code_morse[messages.upper()] + " "

print (text)
