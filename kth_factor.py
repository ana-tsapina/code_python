def factors(n, k): 

    result = []
    x = int(n**0.5)+1

    for divider in range(2, x): 
        if n % divider == 0: 
            result.append(divider)

            quotient = n // divider 
            if quotient != divider:
                result.append(quotient)

   result.sort()

   if (k-1) >= len(result): 
        return -1
    else: 
        return result[k-1]



print(factors(16, 4))