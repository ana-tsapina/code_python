quo = int(input("Enter a number: ")) # Don't forget to typecast!! 

prime = True 


def prime(quo): 
    for i in range(2, quo): 
        if quo % i == 0:
            return False
    return True  

        
def numbers(quo):
    prime_factors = []

    prime(quo)

    for a in range(quo): 
        for b in range(prime_factors): 
            if (a + b)// 2 ==  quo: 
                print(f"{a} \n {b}")


we = numbers(quo)

print(numbers(we))



 # condition for prime: 
# divided by one 
# divided by itself 

## in class code: 

size = int(input())
values = []
for i in range(size): 
    values.append(int(input))



def method1(num): 
    # if num has 2 factors, it is prime 
    counter = 0
    for divider in range(1, num+1): 
        if num % divider == 0: 
            counter += 1
        return counter == 2 # counter compared by two 