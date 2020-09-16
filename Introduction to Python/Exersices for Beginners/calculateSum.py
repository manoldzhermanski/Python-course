def calculate_sum(n):
    previousNumber = 0
    for i in range(n):
        sum = previousNumber + i
        print("Current number:",i,"Previous Number",previousNumber,"Sum:",sum)
        previousNumber = i

try:
    r = int(input())
except:
    print("The range must be a whole number")

calculate_sum(r)
