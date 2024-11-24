def reverse(word): 
  
    if len(word) == 0: 
        return word 
    else: 
        return reverse(word[1:]) + word[0]



test = input("What would you like to reverse? ")
print(reverse(test))