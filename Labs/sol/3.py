def reverseNumber(num):
    reverseNum = 0
    while(num > 0):
        digit = num % 10
        reverseNum = reverseNum * 10 + digit
        num = num // 10

    return reverseNum


print(reverseNumber(12121))
