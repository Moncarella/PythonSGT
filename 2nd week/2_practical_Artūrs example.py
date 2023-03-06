### Only adding things, that were done wrong or differently ###

#######   Task 1   ########
age = int(input("Enter your age:"))
hasDrivingLicence = input("Do you have a driving licence (y/n)?")

result = age >= 18 and hasDrivingLicence == "y"
print("You are able to drive: " + str(result))


#######   Task 2   ########
password = input("Enter your password:")
result = password.__len__() > 7
print("Password accepted: " + str(result))


#######   Task 3   ########
int1str,int2str = input("Enter two integers:").split()
int1 = int(int1str)
int2 = int(int2str)
int1Mod = int1 % 2
int2Mod = int2 % 2

print("Both number are even:",int1Mod == 0 and int2Mod == 0)
print("At least one number is even:",not (intMod != 0 and int2Mood != 0))


########   Task 4   ########
year = int(input("Enter year: "))
leapYear = (year%4 == 0 and year % 100 != 0) or year%400 == 0
print("Leap year:",leapYear)


########   Task 5   ########
dayStr,monthStr,yearStr = input("Enter date:").split()
day = int(dayStr)
month = int(monthStr)
year = int(yearStr)

leapYear = (year%4 == 0 and year % 100 != 0) or year%400 == 0
valid = day > 0 and day < 32 and month > 0 and month < 13 and ((month == 1) or
                                                               (month == 2 and (
    (day < 30 and leapYear == True) or (day < 29 and leapYear == False))) or month == 3)#etc.