

#Extract starting Letter
with open ("./Input/Letters/starting_letter.txt","r") as file:
    content = file.readlines()
    # print (content)
    letter = [name.strip("\n") for name in content]
text = ""
for word in letter:
    text = text + word + "\n"


#extract invited names
with open ("./Input/Names/invited_names.txt","r") as file:
    content = file.readlines()
    invited_names = [name.strip() for name in content]



# for word in invited_names:
    new_letter = text.replace("[name]",word)
    with open(f"./Output/ReadyToSend/letter_for_{word}.txt", "w") as file:
        file.write(new_letter)