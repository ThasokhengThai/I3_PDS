
#Solution 
def describe(*numbers, decimals=2, label="Data"):
    # * used as pointer to indicate that the function can accept a variable number of positional arguments. In this case, the numbers parameter will be a tuple containing all the positional arguments passed to the describe function.
    #arguments are used to pass a variable number of positional arguments to a function. In this case, the numbers tuple will contain all the positional arguments passed to the describe function, which can be used to calculate the count, minimum, maximum, and mean of the numbers.
    if not numbers:
        print(f"{label}: no values")
        return None
    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = round(sum(numbers) / count, decimals)
    print(f"{label}: count={count}, min={minimum}, max={maximum}, mean={mean}")
    return (count, minimum, maximum, mean)

def make_tag(text, **style):
    # ** used as pointer to indicate that the function can accept a variable number of keyword arguments. In this case, the style parameter will be a dictionary containing all the keyword arguments passed to the make_tag function.
    #keyword arguments are used to pass a variable number of keyword arguments to a function. In this case, the style dictionary will contain any additional keyword arguments passed to the make_tag function, which can be used to specify the style attributes of the HTML span tag.
    attrs = ' '.join(f'{key}="{value}"' for key, value in style.items())
    return f"<span {attrs}>{text}</span>"

square = lambda x: x ** 2
is_adult = lambda age: age >= 18
print(describe(12, 7, 30, 4))
print(describe(3.14159, 2.71828, decimals=3, label="Constants"))
print(describe())       
print(make_tag("Hello", color="red", size=14))
print(square(9), is_adult(17), is_adult(21))
print(describe(1, 2, 3, 4, 5, decimals=1, label="Numbers"))