# Display whether a given year is leap year or not

year = int(input("Enter year :"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Yes. Leap Year!")
else:
    print("No. Not a leap year!")
