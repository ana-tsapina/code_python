#Program Goal: build a Python a second python program that can add, subtract, multiply, and divide, and is better than the first calculator 

#Custom Function 

def numericInput(prompt): 

    while True: 
        value = input(prompt)
    try: 
        value = float(value)
        return value 
    except: 
        print(f"{value} cannot be converted into a floating point. ")
        

# print("Welcome to our calculator! :)")

def menu(): 
    menu = """
Calculator Menu Options:

    1. Add 
    2. Subtract 
    3. Multiply
    4. Divide 
    5. Exit Program 


"""

    while True: 

        print(menu)
        user_choice = input("User's Choice: ").lower()
        #.lower() is a string method, edits string to all lower case 

        if user_choice in {'add', '1', ' + '}:
            return 1
        elif user_choice in {'subtract', '2', ' - '}: 
            return 2
        elif user_choice in ('multiply', '3', ' * '):
            return 3
        elif user_choice in ('divide', '4', ' / '):    
            return 4
        elif user_choice in ('exit', ' 5 '): 
            return 5  
        else: 
            print(f"{user_choice} is not a menu option")


    while True: 

        num1 = numericInput("Enter a number: ")
        num2 = numericInput("Enter another number: ")

        answer = 0 

        if menu_result == 1: 
            Print(f"{num1} + {num2} = {answer}")
        elif menu_result == 2: 
            print(f"{num1} - {num2} = {answer}")
        elif menu_result == 3: 
            print(f"{num1} * {num2} = {answer}")
        elif menu_result == 4: 

            try: 
                answer = num1 / num2
                print(f"{num1} / {num2} = {answer}")
            except ZeroDivisionError: 
                print(f"Can't diviide by zero, please try again. ") 

        elif menu_result == 5: 
            print(f"See you later :) ")

        breaks
