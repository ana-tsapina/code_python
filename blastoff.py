def bubble(a_list): 

    swapped = True 

    while swapped: 
        swapped = False
        for i in range(1, len(a_list) -1): 
            if a_list[i] > a_list[i+1]:
                swapped = True
                a_list[i], a_list[i+1] = a_list[i+1],  a_list[i]

    return a_list


print(bubble([1,88,77,2,34,99]))



def in_sort(b_list): 
    i = 1
    while i < len(b_list): 
        j = i 
        while j > 0 and b_list[j] < b_list[j-1]:
            b_list[j], b_list[j-1] = b_list[j-1], b_list[j]
        j = j - 1 

print(in_sort([1,88,77,2,34,99]))