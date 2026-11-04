#Problem 7. Digit Tools  (Medium) 
#Topics: while loops, // and % 

#SOLUTION
def digit(n):
    total = 0
    while n >0:
        total += n % 10
        n //= 10
    return total

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

def is_palindrome(n):
    reversed_n = reverse_number(n)
    return n == reversed_n
#(a) Test the three functions with 2026, 12321 and 9875.
test_number=[2026,12321,9875]
for n in test_number:
    print(f"{n}:digit sum={digit(n)},reversed={reverse_number(n)},palindrome={is_palindrome(n)}")
print()
#(b) Count how many palindromes there are from 10 to 999.
count=0
for n in range(10,1000):
    if is_palindrome(n):
        count+=1
print(f"Palindromes from 10 to 999: {count}")