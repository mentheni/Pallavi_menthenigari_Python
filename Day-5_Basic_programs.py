#!/usr/bin/env python
# coding: utf-8

# 31.	Count words in a sentence

# In[6]:


sent = 'pallavi is very good girl and she is soo good at heart'
sent = list(sent.split(' '))
dic = {}
for word in sent:
    if word not in dic:
        dic[word] = 1
    else:

        dic[word] = dic[word]+1

print(dic)



# 32.	Anagram check

# In[27]:


word1= 'listen'
word2= 'silent2'
d1 = {}
d2 = {}

if len(word1) != len(word2):
    print("not anagram")
else:
    for char1 in word1:
        if char1 not in d1:
            d1[char1]=1
            print(d1)

        else :

            d1[char1] = d1[char1] + 1
    for char2 in word2:
        if char2 not in d2:
            d2[char2]=1

        else :

            d2[char2] = d2[char2] + 1    
#print(d1)
#print(d2)


if d1 == d2 == {}:
    pass

elif d1==d2:
    print("anagram")




# In[29]:


def anagram (l1,l2):
    return sorted(l1) == sorted(l2)

anagram('listennn','silent' )



# 33.	Matrix addition

# In[12]:


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

#result =[[0 for i in range(len(A[0])) ]for i in range(len(A))]
result = []

for i in range(len(A)):
    row = [] 
    for i in range(len(A[0])):
        row.append(0)
    result.append(row)

print(result)


for k in range(len(A)):
    for l in range(len(A[0])):
        result[k][l] = A[k][l] + B[k][l]
print(result)



# 34.	Matrix multiplication

# In[22]:


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
# Generate 0 matrix
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(0)
    result.append(row)
#print(result)  

#do multiplication

for i in range(len(A)):

    for j in range(len(A[0])):

        for k in range(len(B)): # going through each element
            result[i][j] = A[i][k] + B[j][k]
#print(result)


for row in result:
    print(row)#



# 35.	Transpose of a matrix

# In[5]:


A = [[1, 2, 3, 4],
     [4, 5, 6, 6],
     [7, 8, 9, 1]]

rows = len(A)
cols = len(A[0])

#print(row,col)

transpose = []

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(A[j][i]) # 11, 21,31
        #print(row)
    transpose.append(row)

print("Transpose of A:")
for r in transpose:
    print(r)



# 36.	Flatten a nested list

# In[6]:


nested = [[1,2,3],[3,4,5],[6,7,8]]
list1 = []
for lists in nested:
    for l in lists:
        list1.append(l)

print(list1)



# 37.	Find second largest element in a list

# In[10]:


mylist = [3,5,7,9,4,5,8,0]

mylist.sort(reverse = True)
second_large = mylist[1]
print(second_large)


# In[39]:


mylist = [3,5,7,9,4,8,0,0,4,4,4]
n = len(mylist) #7

for i in range(n):
    #print(i)
    for j in range(0,n-i-1):
        #print(j)
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j+1], mylist[j]

mylist = list(set(list(mylist)))
print(mylist)
second_large = mylist[-2]
print(second_large)


# 38.	Find common elements in two lists

# In[46]:


l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4,7,8,9]
result = []
for num in l1:
    if num in l2:
        result.append(num)
print(result)




# 39.	Implement a stack using list

# In[52]:


stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushing", stack)

print("stack poping one element" , stack.pop())

print("stack after pop" , stack)

if stack:
    print("the top element is", stack[-1])
if len(stack)==0:
    print("stack empty")



# 40.	Implement a queue using list

# In[67]:


staclk =[]
stack.append(10)
stack.append(20)
stack.append(30)

print("the queue is", stack)
print("after removing fifo: ", stack.pop(0))
print("the queue after removing 1st element:" ,stack)

if stack:
    print("the 1st element is " ,stack[0])
if len(stack) == 0:
    print("stack is empty")


# In[ ]:




