with open ("file1.txt") as file:
    file1 = file.readlines()

with open("file2.txt") as file:
    file2 = file.readlines()

result = [int(n.strip()) for n in file1 if n in file2]

print (result)


