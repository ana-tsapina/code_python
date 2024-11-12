def factorial(num): 

    if num == 0: 
        return 0 
    elif num == 1: 
        return 1
    else: 
        i = num
        product = num * factorial(num-1)
    
    return product 


print(factorial(3))