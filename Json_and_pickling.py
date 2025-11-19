#!/usr/bin/env python
# coding: utf-8

# 52.	JSON read & write (serialization, deserialization)

# In[1]:


#Serialization

import json
data = {
    "name": "Pallavi",
    "age": 28,
    "skills": ["Python", "SQL", "Support"],
    "is_active": True
}

with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)

with open("data.json", 'r') as file1:
    content = file1.read()
    print(content)


# In[4]:


#Deserialization
import json
with open("data.json", 'r') as file:
    data = json.load(file)
print(data)


# In[2]:


import json

# Convert Python object → JSON string
person = {"name": "John", "city": "Toronto"}
json_string = json.dumps(person)
print(json_string)   # '{"name": "John", "city": "Toronto"}'

# Convert JSON string → Python object
data = json.loads(json_string)
print(data["city"])  # Toronto


# Common Functions
# Function	Description
# json.dump(obj, file)	Write JSON data to a file
# json.dumps(obj)	Convert Python object → JSON string
# json.loads(str)	Convert JSON string → Python object

# 53.	Pickle (save Python objects to file)

# Serialization (Pickling) → Converting a Python object into a byte stream and saving it to a file.
# 
# Deserialization (Unpickling) → Loading that byte stream back into a Python object

# In[12]:


#Serializing
import pickle
data = {
    "name": "Pallavi",
    "age": 28,
    "skills": ["Python", "SQL", "Support"],
    "is_active": True
}

with open("data.pkl", 'wb') as file : # wb is write binary
    pickle.dump(data,file)

with open("data.pkl", 'r') as file1:
    content = file1.read()
    print(content)


# In[15]:


#Desirializing
import pickle
with open("data.pkl",'rb') as file:
    data = pickle.load(file)
    print(data)


# 54.	Generate a text file with random numbers

# In[20]:


import random

with open("random_numbers.txt", 'w') as file:
    for i in range(20):
        number = random.randint(1,100)
        file.write(str(number) + "\n")
with open("random_numbers.txt", 'r') as file1:
    content = file1.read()
    print(content)


# 55.	Merge contents of multiple files into one

# In[38]:


with open("pallavi1.txt", 'w') as file1:
    file1.write("Im pallavi 1")
with open("pallavi2.txt", 'w') as file2:
    file2.write("Im pallavi 2")
with open("pallavi3.txt", 'w') as file3:
    file3.write("Im pallavi 2")


files = ['pallavi1.txt','pallavi2.txt', 'pallavi3.txt']


with open('finalfile.txt', 'w') as outfile:
    for f in files:
        print(f)
        with open(f, 'r') as infile:

            contents = infile.read()
            outfile.write(contents + "\n")
            print(outfile)
with open('finalfile.txt', 'r') as file4:
    finalcontent = file4.read()
    print(finalcontent)


# In[ ]:




