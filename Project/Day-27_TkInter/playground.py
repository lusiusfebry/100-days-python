# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# total = add(1,2,3,4)
# print(total)

def calculate(**kwargs):
    print (kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)


calculate(add=3,multiply=5)