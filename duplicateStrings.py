def duplicate(word1, word2):
    ''' function to find duplicated charcters in two strings 

    arguments: two string values

    return: a list of overlapping strings ''' 

    result = []
    if not word1 or not word2: 
        return [] # one or both strings are empty 
    else: 
        set_word2 = set(word2) 
        
        for character in word1: 
            if character in set_word2: 
                result.append(character)
            
    return sorted(result) 



word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")

final = duplicate(word1, word2)

print(final)