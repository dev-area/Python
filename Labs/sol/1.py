def sumAllDigits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        # num = int(num / 10)
        num = num // 10

    return sum


print(sumAllDigits(333))
