

# 1
def add(a, b):
    return a + b

# 2
def subtract(a, b):
    return a - b

# 3
def multiply(a, b):
    return a * b

# 4
def divide(a, b):
    return a / b

# 5
def square(n):
    return n * n

# 6
def cube(n):
    return n * n * n

# 7
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

# 8
def positive_negative(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

# 9
def largest_two(a, b):
    return max(a, b)

# 10
def largest_three(a, b, c):
    return max(a, b, c)

# 11
def smallest_two(a, b):
    return min(a, b)

# 12
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

# 13
def sum_natural(n):
    return sum(range(1, n + 1))

# 14
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

# 15
def reverse_number(n):
    return int(str(n)[::-1])

# 16
def palindrome_number(n):
    return str(n) == str(n)[::-1]

# 17
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 18
def fibonacci(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# 19
def count_digits(n):
    return len(str(abs(n)))

# 20
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 21
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 22
def power(a, b):
    return a ** b

# 23
def armstrong(n):
    digits = len(str(n))
    total = sum(int(i) ** digits for i in str(n))
    return total == n

# 24
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

# 25
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# 26
def average(a, b, c):
    return (a + b + c) / 3

# 27
def list_sum(a):
    return sum(a)

# 28
def list_max(a):
    return max(a)

# 29
def list_min(a):
    return min(a)

# 30
def count_even(a):
    count = 0
    for i in a:
        if i % 2 == 0:
            count += 1
    return count

# 31
def count_odd(a):
    count = 0
    for i in a:
        if i % 2 != 0:
            count += 1
    return count

# 32
def search_list(a, x):
    return x in a

# 33
def string_length(s):
    return len(s)

# 34
def count_vowels(s):
    count = 0
    for i in s:
        if i.lower() in "aeiou":
            count += 1
    return count

# 35
def reverse_string(s):
    return s[::-1]

# 36
def palindrome_string(s):
    return s == s[::-1]

# 37
def count_words(s):
    return len(s.split())

# 38
def uppercase(s):
    return s.upper()

# 39
def lowercase(s):
    return s.lower()

# 40
def tuple_sum(t):
    return sum(t)

# 41
def tuple_max(t):
    return max(t)

# 42
def tuple_min(t):
    return min(t)

# 43
def leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# 44
def km_to_meter(km):
    return km * 1000

# 45
def meter_to_km(m):
    return m / 1000

# 46
def area_circle(r):
    return 3.14 * r * r

# 47
def area_rectangle(l, b):
    return l * b

# 48
def area_triangle(b, h):
    return 0.5 * b * h

# 49
def simple_interest(p, r, t):
    return (p * r * t) / 100

# 50
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


# FUNCTION CALLS

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Square:", square(5))
print("Cube:", cube(3))
print("Even/Odd:", even_odd(10))
print("Positive/Negative:", positive_negative(-5))
print("Largest:", largest_two(10, 20))
print("Largest:", largest_three(10, 30, 20))
print("Smallest:", smallest_two(10, 5))
print("Factorial:", factorial(5))
print("Natural Sum:", sum_natural(10))
print("Digit Sum:", sum_digits(1234))
print("Reverse:", reverse_number(1234))
print("Palindrome:", palindrome_number(121))
print("Prime:", prime(7))
print("Fibonacci:", fibonacci(7))
print("Digits:", count_digits(12345))
print("GCD:", gcd(12, 18))
print("LCM:", lcm(12, 18))
print("Power:", power(2, 3))
print("Armstrong:", armstrong(153))
print("Celsius to Fahrenheit:", celsius_to_fahrenheit(30))
print("Fahrenheit to Celsius:", fahrenheit_to_celsius(86))
print("Average:", average(10, 20, 30))
print("List Sum:", list_sum([1, 2, 3, 4]))
print("List Maximum:", list_max([10, 20, 5]))
print("List Minimum:", list_min([10, 20, 5]))
print("Even Count:", count_even([1, 2, 4, 5, 6]))
print("Odd Count:", count_odd([1, 2, 4, 5, 6]))
print("Search:", search_list([10, 20, 30], 20))
print("String Length:", string_length("Python"))
print("Vowels:", count_vowels("Python"))
print("Reverse String:", reverse_string("Python"))
print("String Palindrome:", palindrome_string("madam"))
print("Word Count:", count_words("Python is easy"))
print("Uppercase:", uppercase("python"))
print("Lowercase:", lowercase("PYTHON"))
print("Tuple Sum:", tuple_sum((10, 20, 30)))
print("Tuple Maximum:", tuple_max((10, 20, 30)))
print("Tuple Minimum:", tuple_min((10, 20, 30)))
print("Leap Year:", leap_year(2024))
print("Kilometers to Meter:", km_to_meter(5))
print("Meter to Kilometer:", meter_to_km(5000))
print("Circle Area:", area_circle(5))
print("Rectangle Area:", area_rectangle(10, 5))
print("Triangle Area:", area_triangle(10, 5))
print("Simple Interest:", simple_interest(10000, 5, 2))

print("Multiplication Table:")
multiplication_table(5)