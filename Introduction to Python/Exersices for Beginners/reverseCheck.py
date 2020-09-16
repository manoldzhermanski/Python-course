def reverseCheck(number):
    original = number
    rev = 0
    while (number > 0):
        remainer = number % 10
        rev = rev * 10 + remainer
        number = number // 10
    if (original == rev):
        return True
    else:
        return False

print(reverseCheck(121))
