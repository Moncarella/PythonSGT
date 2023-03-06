#######   Task 1   ########

print("Please enter your age:")
agestr = input()
age = int(agestr)

print("Do you have a driver's licence?")
driver = input()

res = age>=18 and driver == "Yes"

print("You are able to drive:" + (str(res)))


#######   Task 2   ########
password = str(input("Please enter your password:"))

res = len(password) >= 8

print("Password accepted:" + (str(res)))


#######   Task 3   ########
integer1 = int(input("Please enter an integer:"))
integer2 = int(input("Please enter an integer:"))
res1 = integer1%2==0 and integer2%2==0
res2 = integer1%2==0 or integer2%2==0

print("Both numbers are even:" + str(res1))
print("At least one number is even:" + str(res2))


########   Task 4   ########
year = int(input("Please enter a year:"))
res = (year%4==0 and year%100!=0) or year%400==0
print("Leap year:" + str(res))


########   Task 5   ########
day = int(input("Please enter day:"))
month = int(input("Please enter month:"))
year = int(input("Please enter year:"))

entereddate = str(day) + "." + str(month) + "." + str(year)

startdate = "01.01.0000"
enddate = "31.12.9999"

res = entereddate > startdate and entereddate < enddate

print("Date valid:" + str(res))