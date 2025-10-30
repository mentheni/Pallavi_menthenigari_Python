#21. Sort a list without using sort()

#bubble sorting
list1 = [2,4,1,7,6]

n = len(list1)
#print(n)
for i in range(n):
    
    for j in range(0,n-i-1):
        if list1[j]> list1[j+1]:
            list1[j], list1[j+1] = list1[j+1] , list1[j]
            #print(list1)
print(list1)  

#selection sorting

arr = [5, 2, 9, 1, 5, 6]

n = len(arr)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap

print("Sorted list:", arr)


#insertion sort

arr = [5, 2, 9, 1, 5, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted list:", arr)

# 22. Print prime numbers in a range
start = 10
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # Check divisors up to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

# 23. Reverse a list without slicing

list1 = [1,2,3,4]
l =[]
le = len(list1)

for i in range(le-1, -1):
    l.append(list1[i])
print(l)

my_list = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(my_list)-1, -1, -1):
    reversed_list.append(my_list[i])

print(reversed_list)


list1 = [1,2,3,4]
reversed_list = list(reversed(list1))
print(reversed_list)

my_list = [1, 2, 3, 4, 5]
n = len(my_list)

for i in range(n // 2):
    my_list[i], my_list[n - i - 1] = my_list[n - i - 1], my_list[i]

print(my_list)


#24. Merge two lists into a dictionary (keys, values)

a = [1,2,3]
b = [3,4,5]
dic = {}

a.append(b)
print(a)

a = [1,2,3]
b = [3,4,5]
dic = {}

for i in range(len(a)):
    print(i)
    dic[a[i]] = b[i]
    
print(dic)

#25.Remove duplicates from a list

list1 = [1,2,1,2,4]
list1 = list(set(list1))
print(list1)


list1 = [1,2,1,2,4]
l = []
for n in list1:
    if n not in l:
        l.append(n)
print(l)





    
