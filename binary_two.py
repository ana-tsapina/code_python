


def bin_search(a_list, target): 
    left = 0 
    right = len(a_list) - 1
    counter = 1 
    

    while left <= right: 
        print(f"Iteration {counter}\n Left Value: {left}\n Right value: {right}")
        mid = (left+right) // 2
        print(f"Mid: {mid} | Fruit at mid: {a_list[mid]}")
        input()
        if a_list[mid] < target: 
            left = mid + 1
        elif a_list[mid] > target: 
            right = mid - 1
        else: 
            return mid 
        
        counter += 1 

    return -1


fruits = ['Apricot', 'Blueberry', 'Cherries', 'Dragonfruit', 'Guava', 'Kiwi', 
        'Lychee', 'Mango', 'Papaya', 'Pear', 'Plum', 'Pineapple', 
        'Pomegranate', 'Tangerine', 'Watermelon']

user_input = input("Enter a fruit: ")
print(f"{user_input} is at index: {bin_search(fruits, user_input)}")
