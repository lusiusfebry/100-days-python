dict_roman = {
    "I" : 1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}



input_string = input()
output = []

for i in input_string:
    output.append(dict_roman.get(i))

print (output)
print (sum(output))