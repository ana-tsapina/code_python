# goal: create a python program that can add, subtract, multiply and divide two numbers

# functional decomposition:
# obtain a way to get two numbers 
#obtain a way to add, subtract, multiply, divide
# do the inputed calculation with the two given numbers 
#output the calculation/result 


print("Welcome to our calculator app!")

#1. grab two numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#2. obtain a way to choose add, subtract, multiply, divide 

choice = input("Choose to either add, subtract, multiply, or divide: ")

if choice == "add": 
    print(num1 + num2)
elif choice == "subtract":
    print (num1 - num2)
elif choice == "multiply": 
    print(num1 * num2)
elif choice == "divide": 
    print(num1/num2) 