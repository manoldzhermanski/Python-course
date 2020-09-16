def exponent(base,exp):
    if exp == 0 :
        print(1)
    else:
        for i in range(1,exp):
            base*=base
        print(base)

exponent(5,0)
