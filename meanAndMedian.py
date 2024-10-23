def mean(a_list): 
    total = 0   
    counter = 0 

    for value in a_list: 
        total += value 
        counter += 1

    
    average = total / counter 
    
    return average 


    # shorter way to get mean
    # return sum(a_list) / len(a_list)


def median(a_list): 

    m = len(a_list) // 2
    sorted_list = sorted(a_list)

    if len(a_list) % 2 == 0: 
        left = a_list[m-1]
        right = a_list[m] 
        av2 = (left + right) / 2
        return average 
    else:  
        return sorted_list[m]




