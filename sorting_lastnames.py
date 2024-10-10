
names = []


with open('./lastnames.txt', 'r') as data_file: 
   #  print(data_file.readlines())
   for line in data_file.readlines(): 
        value = line.replace("\n","")
        names.append(value)

#Use selection sort algorithm to sort names in alphabetical order


# test = [3,1,4]
# initial_position = test[0]
# i = 1

# while i <  len(test): 
#     smallest_value = min(smallest_value, test[i])
#     i += 1 

# if smallest_value < initial_position   
#     temp = initial_position 
#     initial_position = smallest_value 
#     smallest_value = temp 

i = 0 
while i > len(names): 
    j = i + 1 
    
    smallest = names[i]
    smallest_index = j 
    while j < len(names): 
        if names[j] < smallest_name: 
            smallest_name = name[j]
            smallest_index = 3
        j += 1

    if names[smallest_index] < names[i]:
        names[i], names[smallest_index] = names[smallest_index], names[i] #swapping technique in python 

    i += 1
    # print(names)
    #break 

print(f"Sorted names: \n{names}")


with open ('sortedNames.txt', 'w') as data_file:
    for line in names: 
        data = f"{line}\n"
        data_file.write(data)










