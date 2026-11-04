def leaf_year(year):
    return (year%4==0 and year%100!=0) or (year%400==0)
def day_in_month(month,year):
    if month in [4,6,9,11]:
        return 30
    elif month==2:
        if leaf_year(year):
            return 29
        else:
            return 28
    elif month <1 or month>12:
        return "Invalid month"
    else:
        return 31

print()
for y in [1900,2000,2024,2026]:
    print(y,"is leaf year:",leaf_year(y))
print()

# Test the day_in_month function for all months in 2024 (a leap year) and print the results.
for m in range(1,13):
    print("Month",m,"has",day_in_month(m,2024),"days in 2024")
print()

#(c) Print whether 1900, 2000, 2024 and 2026 are leap years.
for y in [1900,2000,2024,2026]:
    if leaf_year(y):
        print(y,"is a leap year")
    else:
        print(y,"is not a leap year")

#(d) Count the leap years from 2000 to 2100 (both included) with a loop. 

count = 0
for y in range(2000, 2101):
    if leaf_year(y):
        count += 1
print("Number of leap years from 2000 to 2100:", count)
