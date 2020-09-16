def findDevisable(lst,devisor):
    print("The given list:",lst)
    for i in lst:
        if( i % devisor == 0 ):
            print(i)

findDevisable([1,5,10,6,5,7],5)
