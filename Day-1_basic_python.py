# 1. Print "Hello, World!"

print("hello world")

# 2. Swap two numbers without a temporary variable
def swap_numbers(a,b):
    a = a + b # 10+20 = 30
    b = a - b #  30 - 20 = 10
    a = a - b
    return a, b

result = swap_numbers(2,3)
print(result)

# 3. Find the factorial of a number (loop)

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = i * f
    return f
    
n = int(input("enter number"))
result = factorial(n)
print(result)

# 4. Fibonacci sequence (loop)

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("enter number"))
for i in range(n):
    print(fibonacci(i), end=" ")

# 5. Check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:   # any even number > 2 is not prime
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # check only odd divisors
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(2))   # True
print(is_prime(9))   # False
print(is_prime(13))  # True
        


#Beginner friendly
def is_prime(n):
   if n<=1:
       return False
   for i in range(2, n):
        if n%i ==0:
            return False
   return True

# Example
print(is_prime(51))   # True
print(is_prime(10))  # False

# 6.Reverse a string
mystring = 'Pallavi'
mylist = list(mystring)

result = mystring[::-1]
print(result)

def reverse_string(mystring):
    l = ''
    for char in mystring:
        l = char + l
    return l

mystring = 'Pallavi'
print(reverse_string(mystring))


# 7. Palindrome check (string & number)
def palindrome(mystring):
    reversed_string = ''
    for i in mystring:
        reversed_string = i + reversed_string
        #print(reversed_string)
    if reversed_string == mystring:
        print("Palindrome")
    else:
        print("Not Palindrome")

mystring = input("enter a string")

palindrome(mystring)

# 8 . Count vowels and consonants in a string

mystring = 'pallavi'

def countalph(mystring):

    vowels = ['a','e','i','o','u']
    constants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']   
    vc = 0
    cc = 0
    for char in mystring:
        if char in vowels:
            vc = vc+1
        else:
            cc = cc+1
    print(vc,cc)
    
countalph('pallavi')


# 9 .Find largest of 3 numbers
numbers = [21,31,41]

numbers.sort(reverse = True)

print(numbers[0])

numbers = [21,31,41,2,3,5,6]

def large_value(numbers):
    large = numbers[0]
    for n in numbers:
        if n > large:
            large = n
    return large

result = large_value(numbers)
print(result)


large = numbers[0]
for n in numbers:
    if n > large:
        large = n
print(large)

# 10 .Sum of digits of a number

def sum_of_digits(n):
    sum = 0
    if n == ' ':
        print("Empty string identified")
    else:
        for i in str(n):
            sum = sum + int(i)
        return sum
    
n = int(input("enter number"))
result = sum_of_digits(n)
print(result)

