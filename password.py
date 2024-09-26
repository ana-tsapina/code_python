#Goal: Create a password generator in Streamlit 

# Required: password length, password criteria, uppercase characters? special character? 
# Generate password that meets requirements 
# Output the generated password  
import random 

# print("Welcome to our password generating app!")

pwd_length = int(input("Enter the length of the password: "))

# Password criteria 
lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

pwd_symbols = lowercase.copy() # list of posible characters for password 

has_upper = input("Include uppercase characters? (yes/no): ")
if has_upper == 'Y' or has_upper == 'y': 
    pwd_symbols.extend(uppercase)

has_special = input("Include special characters? (yes/no): ")
if has_special == 'Y' or has_upper == 'y': 
        pwd_symbols.extend(special)

has_digits = input("Include digits? (yes/no): ")
if has_digits == 'Y' or has_digits == 'y': 
        pwd_symbols.extend(digits)

new_password = "" #Empty string to hold new password 


while len(new_password) != pwd_length: 
    random_symbol = chr(random.choice(pwd_symbols))
    new_password = new_password + random_symbol 

print(f"{new_password} has been generated. ")



