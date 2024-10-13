from random import seed 
from random import randrange 

def mean(a_list):

    average = sum(a_list) / len(a_list)

    return average 

def median(a_list):

    organized = sorted(a_list)
    middle = len(a_list) // 2

    if len(a_list) % 2 == 0: 
        right = organized[middle]
        left = organized[middle-1]
        return (left+right) / 2
    else: 
        return sorted_a_list[middle]





seed(1)
data = [randrange(1,100) for _ in range(randrange(10, 30))]
print(f"The list is: {data}")
print(f"the mean is: {mean(data)}")
print(f"the median is: {median(data)}")