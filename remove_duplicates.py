def remove_duplicate(a_list):

    '''
        function to have a single copy of a character in a list 
  
    argument: 
    a_list: a list with various objects 

    return: 
    new_list: a list with only unique values (no duplicates)

    '''
    new_list = []

    for item in a_list:
        if item not in new_list:
            new_list.append(item)

    return new_list
text = ["a","b","c","c","d","e"]
print(f"test list: {text}")
print(f"duplicates removed: {remove_duplicate(text)}")
