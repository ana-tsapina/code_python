
t_time = int(input("How much time do you have (in minutes)? "))
c = int(input("How many chores do you have to do? "))

task = []
num = 0 

for i in range(c): 
    num += 1
    task.append(int(input(f"How long will {num} task take? ")))

#print(task)

can_do = []
added = 0
j = 0 

# use loop to compare value[0] to t_time
# if less than, add value[1] to value[0], keep going until greater than or equal to 
#if greater than, remove value from value[i] from the added 
# output that 

while i < len(task) and added < t_time: 
    can_do.append(task[i])
    added += task[i]
    j += 1

    if added > t_time: 
        an_do.pop(-1)
    


print(f"You can complete {j} chore(s)!")


# find sum of the time needed to do each chore 
# add the chore values, and each time check if it fits into the time allotted
# if greater than, break 



