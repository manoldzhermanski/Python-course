def multiply_or_sum(num1,num2):
    if num1 * num2 < 1000:
        return num1 * num2
    else:
        return num1 + num2

try:
    number1 = int(input())
    number2 = int(input())
except:
    print("You must enter numbers")

result = multiply_or_sum(number1,number2)
print("Result is:",result)
