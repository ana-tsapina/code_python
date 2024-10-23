def factor(num):
    ''' Create a list of the factors of an int 

    argument: an integer value 

    return: True is prime, otherwise false'''

 
    factors = []

    for divider in range(1, num+1): 
        if num % divider == 0:
            factors.append(divider)

    return factors

def prime(num): 

    return len(factor(num)) == 2  
    


print(factor(13))
print(factor(12))
print(prime(13))
print(prime(12))

