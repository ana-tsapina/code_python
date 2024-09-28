
# x = int(input("Enter your x value: "))
# y = int(input("Enter your y value: "))



point = input("Enter your x and y value: ")

point = point.split(' ')

# fixed_point = []
# for value in point: 
#     fixed_point.append(int(value))


point = list(map(int, point))
print(point)


x,y = point

print(f"x is {x}")
print(f"y is {y}")

if x > 0:  

    if y > 0: 
        print(f"The point of ({x},{y}) is in Quadrant 1")
    else: 
        print(f"The point of ({x},{y}) is in Quadrant 4")
else: 
    if y > 0: 
        print(f"The point of ({x},{y}) is in Quadrant 2")
    else: 
        print(f"The point of ({x},{y}) is in Quadrant 3")

