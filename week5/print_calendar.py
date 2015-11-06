#!/usr/bin/env python3

'''
Write a program that displays the calendar
for a given month of the year.
The program prompts the user to enter the year
and the month, and then it displays the
entire calendar for the month.
'''

# A stub for printMonth may look like this 
def printMonth(year, month):
    print("\n") 
    printMonthTitle(year, month)
    printMonthBody(year, month)
    print("\n")

# A stub for printMonthTitle may look like this 
def printMonthTitle(year, month):
    month = "{:>15}{:>5}".format(getMonthName(month), year)
    print(month)
    print("----------------------------")
    week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fry", "Sat"]
    print(" ".join(week))

# A stub for getMonthBody may look like this 
def printMonthBody(year, month):
    start = getStartDay(year, month)
    i = 1 - start
    totalDays = getNumberOfDaysInMonth(year, month)

    while i <= totalDays:
        day = i if i > 0 else "x"
        end = "\n" if (start + i) % 7 == 0 else ""
        print("{:<4}".format(day), end=end)
        i += 1

# A stub for getMonthName may look like this 
def getMonthName(month): 
    months = [
        None,
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "Dicember"
    ]
    return months[month]

# A stub for getStartDay may look like this 
def getStartDay(year, month):
    START_DAY_JAN_1800 = 3    
    totalDays = getTotalNumberOfDays(year, month)
    return (START_DAY_JAN_1800 + totalDays) % 7

# A stub for getTotalNumberOfDays may look like this 
def getTotalNumberOfDays(year, month): 
    days, total = 365, 0
    for y in range(1800, year):
        total += (days + 1) if isLeapYear(y) else days
    for m in range(1, month):
        total += getNumberOfDaysInMonth(year, m)
    return total

# A stub for getNumberOfDaysInMonth may look like this 
def getNumberOfDaysInMonth(year, month):
    months = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = months[month]
    return (days + 1) if month == 2 and isLeapYear(year) else days

# A stub for isLeapYear may look like this 
def isLeapYear(year): 
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    # Prompt the user to enter year and month 
    year = eval(input("Enter full year (e.g., 2001): "))
    month = eval(input((
        "Enter month as number between 1 and 12: ")))

    # Print calendar for the month of the year
    printMonth(year, month)

if __name__ == "__main__":
    main()