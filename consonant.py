def consonant(word):
    '''
    purpose: 
        find consonants in inputted word 
    argument: 
        alphabetic input 

    return: 
        number of consonants in string
    '''

word = input("Enter a word: ")

ctr = 0 
for character in word: 
    word = word.lower()
    if word.isalpha() and (character) not in {'a','e','i','o','u'}:
        ctr += 1

print(f"There are {ctr} consonants in your word!")


