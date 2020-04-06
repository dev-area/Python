# def getMax(a, b):
#     return a if a > b else b


def getMax3(a, b, c):
    def getMax(a, b):
        return a if a > b else b

    return getMax(getMax(a, b), c)


# print(getMax(100, 10))
print(getMax3(100, 10, 200))
