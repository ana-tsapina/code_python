# linear: 


def lin(arr, target): 
    if not arr: 
        return -1
    else: 
        for i in range(len(arr)): 
            if arr[i] == target: 
                return i 
    


def bin(arr, target): 

    left = 0 
    right = len(arr) -1 

    while i < len(arr): 

        middle = (right + left) // 2

        if arr[middle] == target: 
            return middle 
        elif arr[i] > middle: 
            left = arr[i] + 1
        elif arr[i] < middle: 
            right = arr[i] - 1
        else: 
            return -1 


def selection(array, result = []): 

    if not array: 
        return result
    else:  
        smallest = array[0]
        small_index = 0



    for i inrange (a, len(array): 
        if array[i] < smallest: 
            smallest = array[i]
            small_index = i


    result.append(array.pop(small_index))


    return selection(array, result)



    def bubbble(a_list): 
        
        swapped = True

        for i in range (1, len(a_list)-1): 
            if a_list[i] < a_list[i-1]:
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i]

        return a_list
        

print(in_sort([1,88,77,2,34,99]))