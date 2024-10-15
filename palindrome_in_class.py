def isPalindrome(word:str) -> bool: 
    #def isPalindrome(word)
    #base case -> empty string are palindromes
    if not word: # if len(word) == 0: 
        return True 
    #Base case #2 -> a single character is a palindrome 
    elif len(word) == 1: 
        return True
    # Base case #3 -> strings with two  or three characters
    elif len(word) <= 3: 
        return word[0] == [-1]
    else: 
       
    # for i in word: 
    #     right = word[i]
    #     left = word[i*1 -1]
        word2 = word[::-1]
        return word2 == word 
        # if word2 == word: 
        #     return True 
        # else: 
        #     return False     

        # the length of the word is over 3 
        #S1: split in middle and compare 
        #s2: reverse the word into a seperate variable, compare equality 
        #s3: traverse forwards and backwards for equality 
    # return call 


#trying to prove that it is not a palindrome below: 

    i = 0
    j = len(word) - 1

    while i < j: 
        if word[i] != word[j]:
            return false 

    i += 1
    j -= 1



text = input("Enter your word: ")

print(isPalindrome(text))

# flipped: 
# for i in range (-1, -1* len(word)-1, -1:)
# flipped += word[i]
  






