
# 26.	Linear search implementation




list1 = [1,2,3,4,5,6]
search = 6

for i in range(len(list1)):
    if list1[i] == search :
        print(i)


# 27.	Binary search implementation




# list1 = [1,2,3,4,6,8,11,25]

target = 11

left = 0
right = len(list1)-1
while left <= right:
    mid = (left+right)//2
    if list1[mid] == target:
        print(f"target is {mid}")
    elif list1[mid] > target:
        left = mid + 1
    else:
        right = mid -1

print("-1")





arr = [1,2,3,4,6,8,11,25]

target = 11

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found


# 28.	Bubble sort algorithm




#this is wrong, it is only iterating once.
list1 = [2,6,4,3,5,8,1]

for i in range(0,len(list1)-1):
    #print(i)
    if list1[i] > list1[i+1]:
       list1[i] , list1[i+1] = list1[i+1], list1[i]
print(list1)





list1 = [2,6,4,3,5,8,1]
n = len(list1)
for i in range(n):
    for j in range(0, n-i-1):
        if list1[j] > list1[j+1]:
            list1[j] , list1[j+1] = list1[j+1], list1[j]
print(list1)


# 29.	Insertion sort algorithm

# In[ ]:





# 30.	Selection sort algorithm

# In[5]:


2024 % 400


# In[6]:


2024 % 4 


# In[10]:


2000%400


# In[ ]:




