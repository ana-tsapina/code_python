hour = int(input("What hour is it? "))
min = int(input("What are the minutes? "))


if (9 <= hour < 18):
    print("The register's office is open")
elif (hour == 18 and 0 <= min < 30):
    print("The register's office is open")
else:
    print("The register's office is closed")
    