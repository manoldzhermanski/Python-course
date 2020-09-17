def calculateCubeSum(n):
    if n <= 0 :
        print("Invalid input: Must enter a positive integer")
    else:
        total = 0
        for i in range(1,n):
           total += (i*i*i)
        return total

print(calculateCubeSum(3))
