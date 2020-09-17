import math
def calculateArea(r):
    return (math.pi * r * r)

try:
    radius = float(input())
except:
    print("Invalid input")

print(calculateArea(radius))
