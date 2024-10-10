def consonant(word, vowel = False):
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

    if not vowel: 
        
        return ctr
    else: 
            for character in word: 
                word = word.lower()
                if word.isalpha() and (character) in {'a','e','i','o','u'}:
                    ctr += 1
        
            return ctr 

print(f"There are {ctr} consonants in your word!")


