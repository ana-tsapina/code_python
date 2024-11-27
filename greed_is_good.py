minutes = int(input())
tasks = int(input())
chores = []


for i in range(tasks): 
    current_chore = int(input())
    chores.append(current_chore)

chores.sort()
task_counter = 0 
i = 0 

while minutes > 0: 
    if chores[i] > minutes: 
        break 
    else: 
        minutes -= chores[i]
        task_counter += 1
        i += 1

print(task_counter)




