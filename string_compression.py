def zip(item)

    count = 0
    new = ''

    for i in item: 
        if item[i] == item[i+1]
            count += 1
        else:
            new += item[i-1]
            new += str(count)
            count = 1


    new += item[-1] + str(count)


    if len(new) :
