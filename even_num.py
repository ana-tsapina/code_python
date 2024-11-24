import time 
def new(index): 
    seq = [0,1]
    for i in range(index): 
        seq.append(seq[-1] + seq[-2])
    return seq[-2]



def fibonacci(index): 

    if index <= 1: 
        return index
    else: 
        return fibonacci(index-1) + fibonacci(index-2)



rec = time.time()


print(fibonacci(8))
print("speed: " + str(time.time()-rec))
print(new(8))
it = time.time()
print("speed:") + str(time.time()-it)