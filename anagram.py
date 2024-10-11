 
''' determines if two arguments are anagrams 

    argument: 
        word1: alphabetical, lowercase input 
        word2: alphabetical, lowercase input 

    return: 
        boolean value of True, if words are anagrams, False if no

'''

    #solution one: 
    # if len(word1) != len(word2): 
    #     return False
    # else: 
    #     for character in word1: 
    #         if word1.count(character) != word2.count(character): 
    #             return False 
    # return True 

def anagram2(word1, word2):

    if len(word1) != len(word2): 
        return False
    else: 
        list_word1 = sorted(word1)
        list_word2 = sorted(word2)

    for i, character in enumerate(list_word1): 
        print(f'i: {i}')
        print(f"character: {character}")
        print(f'list_word2[i]: {list_word2[i]}')
        if list_word2[i] != character: 
            return False 

word = anagram2(input(),input())
print(word)


