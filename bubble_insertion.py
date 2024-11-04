''' Let A be a list, N be the length of A 
repeat until swapped is false 
    swapped = false 
    for i = 1 to N-1 (inclusively) 
    if A[i-1] > A[i] then 
        swap(A[i-1], A[i])
        swapped = true 
'''

def bubble(a_list):

    swapped = True 
    while swapped: 
        swapped = False 

        for i in range(1, len(a_list)): 
            if a_list[i-1] > a_list[i]: 
                a_list[i-1], a_list[i]  = a_list[i], a_list[i-1]
                # how to do mutable swap

                # secondary swap using temporary variable 
               # temp = a_list[i]
                #a_list[i] = a_list[i-1]
               # a_list[i - 1] = temp 
            swapped = True 

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(f"The fruit list before sorting: {fruits}")
print(f"The fruit list after sotring: {bubble(fruits)}")

'''
Let A be a list, i and j both be indexes

i = 1

while i < length(A)

    j = i 
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j = j - 1
        i = i + 1
''' 

def in_sort(a_list): 

    i = 1 
    while i < len(a_list): 
        j = i 
        while j > 0 and a_list[j-1] > a_list[j]:
            a_list[j-1], a_list[j]  = a_list[j], a_list[j-1]
            j -= 1 

    i += 1 

    pass 
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(f"The fruit list after sorting: {in_sort(fruits)}")