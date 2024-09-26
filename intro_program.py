# first python program 

first_name = input("Enter your first name: " )
last_name = input("Enter your last name: ")

birth_year = int(input("Enter your birth year: "))

age = 2024 - birth_year

print(first_name, last_name, age) 

message = f"Hello {first_name} {last_name}.\n You are {age} years old"

print(message)

if age >= 19: 
    print("You are old enough to drink!")
else: 
    print("You are not old enough to drink!")
