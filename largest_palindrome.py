
largest = 0
    
for left in range(100,1000):
    for right in range(100, 1000):
        product = left * right
        if  str(product) == str(product)[::-1]:
            largest = max(largest, product)

print(largest)






      


