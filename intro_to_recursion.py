def r_sum(num):
    #Base Case: 
    if num == 0: 
        return 0 
    elif num == 1: 
        return 1
    else:  
        return num + r_sum(num-1)

print(r_sum(10))