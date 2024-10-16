from random import randrange


def css(text): 

    cvs = text.split(',')

    a_list = []
    for item in cvs: 
        a_list.append(int(item))

    return a_list


def second(start, end, frequency):
    if start < end and frequency > 0: 
        a_list = []
        for _ in range(frequency): 
            new_value = randrange(start, end+1)
            a_list.append(new_value)
        return a_list
    else: 
        return []

print(css("1,2,4,5"))
print(second(1, 1000, 30))