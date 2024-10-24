def linSearch(seq, target): 


    if not seq: 
        return -1
    else: 
        for i in range(len(seq)): 
            if seq[i] == target: 
                return i 
        else: 
            return -1 

from random import seed 
from random import randrange
    
seed(1)
seq = [randrange(1, 100) for x in range(20)]
print("Random list: \n", seq)


print(18, linSearch(seq, 18))