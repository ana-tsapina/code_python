
def bubble(a_list): 
    swapped = True 

    while swapped: 
        swapped = False 
         
        for i in range(1, len(a_list)): 
            if a_list[i-1] > a_list[i]: 
              

                temp = a_list[i]
                a_list[i] = a_list[i-1]
                a_list[i-1] = temp 
                swapped = True 
    return  a_list

def in_sort(a_list): 

    i = 1
    while i < len(a_list): 
        j = i
        while j > 0  and a_list[j-1] > a_list[j]: 
            a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            j = j - 1
            i += 1
    return a_list


fruits = [
    "Mango", "Kiwi", "Pomegranate", "Blueberry", "Dragonfruit",
    "Papaya", "Tangerine", "Pear", "Lychee", "Plum",
    "Guava", "Apricot", "Cherries", "Pineapple", "Watermelon"
]

a = bubble(fruits.copy())
b = in_sort(fruits.copy())

print(f"post: {a}")
print(f"new: {b}")
    