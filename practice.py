# #Q1
# def factor(num):

#     count = 0
#     for i in range(1, num+1): 
#         if num % i == 0: 
#             count += 1

#     return count 
# x = int(input("Enter your value: "))

# for i in range(0, x+1):
#     answer = factor(x)

# print(f"The number of factors N has is: {answer}")


# def clean(word): 
#     new = ""

#     for character in word: 
#         if character.isalpha(): 
#             new += character.lower()
    
#     return new


# rah = input("enter: ")

# print(clean(rah))

def factor(num): 
    
    yes = []
    for divider in range(1, num+1): 
        if num % divider == 0: 
            yes.append(divider)

    return yes 

def prime(num): 
    return len(factor(num)) == 2

print(factor(14))
print(prime(14))


