hour = int(input("What hour is it? "))
min = int(input("What are the minutes? "))

if (hour > 24):
    print("Error")
    exit() #attempt to quit program if input is wrong / maybe try using some sort of loop? 
if (min > 59):
    print("Error")
    exit()

if (9 <= hour < 18):
    print("The register's office is open")
elif (hour == 18 and 0 <= min < 30):
    print("The register's office is open")
else:
    print("The register's office is closed")
    
    if (9 <= hour < 18):

