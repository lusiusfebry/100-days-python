import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv", )

nato_alphabetic = {row.letter: row.code for (index,row) in data.iterrows()}

user_input = input("Enter your name : ").upper()

phonetic_code = [nato_alphabetic[word] for word in user_input]

print(phonetic_code)
