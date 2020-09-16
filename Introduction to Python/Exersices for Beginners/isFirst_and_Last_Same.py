def isFirst_and_Last_Same(lst):
    print("Given list:",lst)
    fstEl = lst[0]
    lstEl = lst[-1]
    if (fstEl == lstEl):
        return True
    else:
        return False

print("Result is:",isFirst_and_Last_Same([1,2,3,4,5,1]))
