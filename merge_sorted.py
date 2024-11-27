def merge(list1, list2):

    if not list1: 
        return list2
    if not list2: 
        return list1 

    if list1[0] < list2[0]: 
        return list1[0] + merge(list1[1:], list2)
    else: 
        return list2[0] + merge(list1, list2[1:])









print(merge([1,2,3], [2,2,2]))