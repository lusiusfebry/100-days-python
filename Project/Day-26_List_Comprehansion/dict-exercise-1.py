sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# lst = sentence.split()
# print(lst)
result = {word:len(word) for word in sentence.split()}
print(result)


