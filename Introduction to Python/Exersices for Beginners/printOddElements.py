def printOddElements(word):
    for i in range(len(word)):
        if i % 2 == 0:
            print(word[i])

result = str(input())
printOddElements((result))
