def palidrome(word): 
    '''
    checks if argument is palindome

    argument: 
        word: alphabetical based string 

    return
        a boolean value, true if palindrome, false if not

    '''

    return word == word[::-1]


    print(is_palindrome(print("enter a word: "))), 

def is_palindrome(text): 

    '''
    Checks if argument is a palindrome 


    argument: 
    text: alphabetical based string 

    return: 
        boolean value, true if palindrome, false if not 
    '''

    if not text: 
        # in the case that string is an empty string 
        return True 
    elif len(text) < 4: 
        return text[0] == text[-1]
    else: 
        midpoint = len(text) // 2
        # if the length is odd, we can ignore middle most character 
        for i in range(0, midpoint):
            left = text[i]
            right = text[-1*i -1]

            if left != right: 
                return false
                # return in loop will autoterminate loop 
        return True 


        