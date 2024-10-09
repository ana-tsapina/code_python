def string_cleaner(text):

'''
    to clean a string with non alpha characters and put all characters in lower case 

arguments: 
    ext: string argument that is to be cleeaned

returns 
    string object with lowercase, alphabetical characters 
'''
    result = " " #grow empty string to string with alphabetical characters
    for character in text: 
            if character.isalpha():
                result += character.lower()



    return result 

#end of string_cleaner


value = string_cleaner("hEll0, woRLD")
print (f"Value is:{value}")

