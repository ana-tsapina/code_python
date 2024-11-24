def pal(word): 

    if len(word) <= 1: 
        return True
    elif word[0] == word[-1]: 
        return pal(word[1:-1])
    else: 
        return False


selected = input("Enter a word: ")
print(pal(selected))
