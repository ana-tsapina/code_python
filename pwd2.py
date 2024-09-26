#Goal: create enhanced password generator using streamlit 

import streamlit as st

import random 

st.header("Password Maker")
st.write("This application will generate a password based on the desired criteria! :D")

pwd_length = st.number_input(
    label = "Set Password Length",
    min_value = 8, 
    step = 1, 
    key = "password_length"

)

lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

pwd_symbols = lowercase.copy() # list of posible characters for password 

upper_toggle = st.toggle("Include uppercase characters ")
if upper_toggle == True: 
    pwd_symbols.extend(uppercase)

special_toggle = st.toggle("Include special characters: ")
if special_toggle: 
    pwd_symbols.extend(special)

digit_toggle = st.toggle("Include numbers ")
if digit_toggle: 
    pwd_symbols.extend(digits)


make_pwd_button = st.button("Generate Password! ")
if make_pwd_button: 
    new_password = ""


while len(new_password) != pwd_length: 
    random_symbol = chr(random.choice(pwd_symbols))
    new_password = new_password + random_symbol 

print(f"{new_password} has been generated. ")
st.write(f"{new_password} has been generated")



