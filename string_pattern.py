
num = int(input("Please enter a number: "))

def create_line(num):

    text = ''
    for i in range(1, num+1): 
        if i % 2 == 0: 
            text += '0'
        else: 
            text += '1'
    return text 

def output_pattern(num): 

    for i in range(1, num+1): 
        print(create_line(i))

print(output_pattern(num))



