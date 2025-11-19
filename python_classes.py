#!/usr/bin/env python
# coding: utf-8

# 56.	Class for student (attributes: name, age, marks)

# In[3]:


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Marks : {self.marks}")

#create objects of students class
s1 = Student("Pallavi",32, 100)
s2 = Student("Pooja", 22, 90)

s1.display()
print()
s2.display()


# 57.	Inheritance example (base class & derived class)

# In[8]:


#base class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")

#derived class
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks
    def display(self):
        #reuse base class method
        super().display()
        print(f"marks : {self.marks}")

s1 = Student("pallavi", 32, 100)

s1.display()



# 58.	Polymorphism with methods

# Here:
# 
# All three classes have a method named flight()
# 
# Each class gives its own definition of how that method works.

# In[1]:


class Bird:
    def flight(self):
        print("Some birds can fly but some of them cant fly")
class Sparrow(Bird):
    def flight(self):
        print("sparrow can fly high in the sky")
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly")




# In[3]:


bird1 = Bird()
bird2 = Sparrow()
bird3 = Ostrich()

for b in (bird1, bird2, bird3):
    b.flight()


# 59.	Encapsulation example with private variables

# In[4]:


class Student:
    def __init__(self, name, age):
        self.name = name          # public variable
        self.__age = age          # private variable (note the double underscore)

    # Public method to access private variable
    def get_age(self):
        return self.__age

    # Public method to modify private variable safely
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")

# Create object
s1 = Student("Alice", 20)
s1.display()

# Access private variable directly (❌ not allowed)
# print(s1.__age)   # This will raise an AttributeError

# Access using getter (✅ allowed)
print("Accessing age via getter:", s1.get_age())

# Modify using setter (✅ allowed)
s1.set_age(25)
s1.display()

# Try setting invalid age
s1.set_age(-5)
