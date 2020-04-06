# Create a function ‘gr_than’ that takes a
# number N as parameter and returns
# a function to test if another number is greater
# than N – use lambda expression


def ge_then(num):
    return lambda n: n > num


a = ge_then(5)
print(a(7))
