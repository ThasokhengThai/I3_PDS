#Problem: Temperature Converter
#There are two type of function : return function and non-return function
#Parameter is the prior information that we need to pass to the function
#round_to=1 note: this is a default parameter, if the user does not provide a value for round_to, it will default to 1
#farenheit=(celcius*9/5)+32 is local variable, it is only accessible within the function


def celcius_to_farenheit(celcius,round_to=1):
    farenheit=celcius*9/5+32
    return farenheit
print(celcius_to_farenheit(43),"F")


def farenheit_to_celcius(ferenheit,round_to=1):
    celcius=(ferenheit-32)*5/9
    return celcius
print(farenheit_to_celcius(109.4),"C")

#Methode 2 : using non-return function
def celcius_to_farenheit(celcius,round_to=1):
    farenheit=celcius*9/5+32
    print(farenheit)
celcius_to_farenheit(43)

#Methode3: using non-return function with round_to parameter
def celcius_to_farenheit(celcius,round_to=1):
    farenheit=celcius*9/5+32
    print(round(farenheit,round_to))  
celcius_to_farenheit(47,2) 


#Section2: create a table of celcius and farenheit
# ---------------------------------------------------------------------------
# Problem 3 (Easy) · Temperature converter
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(c, round_to=1):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return round(c * 9 / 5 + 32, round_to)


def fahrenheit_to_celsius(f, round_to=1):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return round((f - 32) * 5 / 9, round_to)


print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))

print(celsius_to_fahrenheit(36, 3), "°F")

#what is c:5? and (c):6
#answer: c:5 is a format specifier that indicates the value of c should be printed with a minimum width of 5 characters. If the value of c has fewer than 5 characters, it will be right-aligned and padded with spaces on the left to make up the width. If c has more than 5 characters, it will be printed as is without truncation.
#answer: (c):6 is a format specifier that indicates the value of c should be printed with a minimum width of 6 characters. If the value of c has fewer than 6 characters, it will be right-aligned and padded with spaces on the left to make up the width. If c has more than 6 characters, it will be printed as is without truncation.
