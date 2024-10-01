
names = []


with open("./lastnames.txt", "r") as data_file: 
   #  print(data_file.readlines())

   for line in data_file.readlines(): 
    value = line.replace("\n","")
    names.append(value)


    print(names)

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
    print(f"names[{i}] is {names[i]}")
    i += 1

    









