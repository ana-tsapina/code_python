def binSearch(array, target): 
    left = 0 
    right = len(array)-1

    while left <= right: 
        middle = (left+right) // 2

    if array[middle] == target: 
        return middle 
    else: 
        if array[middle] < targer: 
            left = middle + 1
        else: 
            right = middle - 1 
    else: 
        return -1 
