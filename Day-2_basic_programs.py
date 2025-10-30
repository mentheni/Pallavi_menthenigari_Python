
# 11 . Check Armstrong number


def amstrong(n):
    s = 0        
    for num in str(n):
        s = int(num)**3 + s
        
    if s == n:
        print("Amstrong number")
    else:
        print("Not Amstrong number")
    
n = int((input("enter number")) )       
result = amstrong(n)
result

# 12. Print multiplication table

  import math as m
def multiplication(n):
    for i in range(1,11):
        
        print(f"{n} * {i} = {n*i}")

n = int(input(" Enter number"))
result = multiplication(n)
result


#13. Convert Celsius to Fahrenheit
# 1c = 33.8 f

def celious_to_fh(n):

    result = (33.8) * n

    return result  

celcius = int(input("Enter celcius"))
celious_to_fh(celcius)



# 14. Find even and odd numbers in a list

def even_odd(list1):
    even = []
    odd  = []
    for num in list1:
        if int(num)%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print(f" Event list id {even} and Odd list is {odd}")

list1 = [1,2,3,4,5,6,7,8,9]
even_odd(list1)

# 15.Find largest and smallest element in a list

def small_large(list1):
    for num in list1:
        if num == '':
            list1.remove(num)
        else:
            pass 
    list1 = list(set(list1))
    list1.sort()
    #print("I'm inside", list1)
    small = list1[0]
    large = list1[len(list1)-1]
    print(f"Small number is {small}, large number is {large}")
    
            
list1 = ['',1,2,3,4,5,6,7,8,9,22,22,'']
#print(small_large(list1))

#without using sort
numbers = [1,2,3,4,5,6,7,8,9,22,22]
small = numbers[0]
large = numbers[0]
for num in numbers:
    if num > large:
        large = num
    if num < small:
        small = num
print(small,large)

# 16.Check leap year
import calendar as cal
def leap(year):
    if cal.isleap(year):
        print(f" {year} is leap year")
    else:
        print(f" {year} is not leap year")
year = int(input("Enter your year"))    
leap(year)

# not using cal function

if (year % 4 ==0 and year % 100 !=0) or (year % 400 == 0):

    print(f" {year} is leap year")
    
else:
    print(f" {year} is not leap year")
    


#17. Count frequency of characters in a string (dict)
mystring = 'pallaviiiiiii'
dict1 = {}
for char in mystring:
    if char in dict1:
        dict1[char] =  dict1[char] + 1
    else :
        dict1[char] = 1
print (dict1)

# 18. Check if a substring exists in a string

fullstring = 'my name is pallavi and im dong well'
substring = 'pallavi'

fullstring = fullstring.split(' ')

for sub in fullstring:
    if sub == substring:
        print(sub)

#19. import random as rd

r = rd.randrange(1,100,2)
print(r)
r1 = rd.randint(1,100)
print(r1)
r2 = rd.sample(range(1,101),10)
print(r2)

#20. Find GCD and LCM of two numbers

# GCD without math library
a = 12
b = 18

# Euclidean algorithm
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

print("GCD of", a, "and", b, "=", gcd(a, b))
print("LCM of", a, "and", b, "=", lcm(a, b))





