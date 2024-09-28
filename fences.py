from math import ceil
section1 = input("Enter section 1: ")
section2 = input("Enter section 2: ")
section3 = input("Enter section 3: ")



#processing -> assumes that the length of each section is entered in string format

cans = len(section1) + len(section2) + len(section3)

boxes = ceil(cans/12)

leftover = 12*boxes - cans
total_cost = 14.95 * boxes 

print(f"We needed {cans} paint cans. ")
print(f"We have {leftover} leftover. ")
print(f"The project costs ${total_cost}. ")


