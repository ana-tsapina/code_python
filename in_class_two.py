def fib(n): 
    memory = {0:0, 1:1}

    def helper(n):
        if n in memory: 
            return memory[n]
        else: 
            memory[n] = helper(n-1) + helper(n-2)
            return memory[n]

    return helper(x)

    print(f"The {10} number of the fibonacci sequence is: {fib{10}}") 
