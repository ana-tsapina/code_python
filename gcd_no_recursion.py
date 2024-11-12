def gcd(int1, int2): 

    for i in range(min(int1, int2), 0, -1): 
        if (int1  % i == 0) and (int2 % i == 0) : 
            return i

print(gcd(8,12))
       


def gcf(int1, int2): 

    factors = [] 
    greatest = 0

    for i in range(min(int1,int2), 0, -1): 
        if (int1  % i == 0) and (int2 % i == 0) : 
            factors.append(i)

    j = 1 
    for j in factors: 
        if factors[j] > factors[j-1]: 
            greatest = j 

        return greatest 

print(gcf(8,12))