def exponent(base, ex): 
    
    if ex == 1:
        return base 
    elif ex == 0: 
        return 1
    else: 
        return base * exponent(base, ex-1)


base = 2 
ex = 3 
print(exponent(base, ex))
