#!/usr/bin/env python
# coding: utf-8

# 48.	File handling – read a file

# In[4]:


file = open("Pallavi.txt" , "r") # File should be in same location as this script
content = file.read()
print(content)


# In[3]:


with open("pallavi.txt", "w") as file:
    file.write("This is interview prep line")

file = open("pallavi.txt","r")
content = file.read()
print(content)


# 49.	File handling – write to a file

# In[86]:


# use "with" to having to not close file after reading/writing file


with open("Pallavi.txt", 'w') as file:
    file.write("this is 1st new line added to file \n")
    file.write("this is 2nd new line added to file \n")
    file.write("this is 3rd line added to file \n")

with open("Pallavi.txt", 'r') as file:
    content = file.read()
print(content)

# above code is easring previous file and adding above lines in file.
# to append new lines to existing code use 'a'


# In[87]:


# appending lines to file

with open("Pallavi.txt", 'a') as file:
    file.write("This is 4th line in the file \n")
    file.write("This is 5th line in the file \n")
    file.write("This is 6th line in the file \n")
with open("Pallavi.txt", 'r') as file:
    content = file.read()
    print(content)


# 50.	File handling – count lines, words, characters

# In[5]:


with open("Pallavi.txt", 'r') as file:
    lines = file.readlines()
    #print(len(lines))
    word = 0
    char = 0
    for line in lines:
        word = word + len(line.split(' '))
        char = char + len(line)
print ("lines", len(lines))
print(word)
print(char)



# 51.	File handling – copy contents from one file to another

# In[89]:


with open("Pallavi.txt", 'r') as file:
    content = file.read()
print(content)

with open("Pallavi_new.txt", 'w') as file1:
    file1.write(content)

with open("Pallavi_new.txt", 'r') as file2:
    final_content = file2.read()

print (final_content)


# In[6]:


with open("Pallavi.txt", 'r' ) as file :
    content = file.readlines()
    print(content)







