
def genfilterby(n):
    # expresion for item in n if
    def filterBy(ls):
        # return lambda item: item % n == 0
        return list(filter(lambda item: item % n == 0, ls))

    return filterBy


fil = genfilterby(3)
print(fil)
z = [2, 3, 4, 5, 6, 7, 8]
print(fil(z)) 		# prints [3,6]
