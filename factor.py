def is_divisible(num1, num2)
''' checks if num1 is divisible by num2 

args: 
num1: numerator, integer
num2: denominator, integer

return: 
true if num1 is divisble by num2, otherwise false
'''

retun num1 % num2 == 0

def factor_count(number): 

    ''' determines number of factors the argument ha
    
    args: 
    number: integer whose factors are being determined
    
    returns: 
    
    an integer, total amount of factors the argument has'''

counter = 0

for divider in range(1, number+1): 
    if is_divisible(number, divider)
    # if number % divider == 0: 
        counter += 1

    return counter  

upper_limit = int(input("Enter N: "))

for num in range(1, upper_limit)
    factor_size = factor_count(num)





