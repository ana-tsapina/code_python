def r_sum(num): 
    # Base Case #1, num = 0 

    if num == 0: 
        return 0 
    #Base Case #2, num is 1 
    elif num == 1: 
        return 1
    else: 
        return num + r_sum(num-1) # before you can solve, you need to know the result of the previous instance 
    # end of sum 

print(f"Sum of all numbers from 1 to 10: {r_sum(10)}")    