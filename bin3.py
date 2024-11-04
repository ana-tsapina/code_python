def bin_search(a_list, target):

    left = 0
    right = len(a_list) - 1
    counter = 1

    while left <= right: 
        print(f"iteration {counter}\n left value: {left}\n  Right value: {right}")
        mid = (left+right) // 2
        print(f"--Mid: {mid} | Fruit @ mid: {a_list[mid]}")
        input()

        if a_list[mid] < target: 
            left  = mid + 1
        elif a_list[mid] > target: 
            right = mid - 1 
        else: 
            return mid
        
        counter += 1 
    
    return -1 





fruits = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli fruit", "watermelon",
    "blueberry", "blackberry", "cantaloupe", "dragon fruit", "passion fruit"
]
user_input = input("Enter target fruit name: ")
print(f"{user_input} is located at index {bin_search(fruits, user_input)}")