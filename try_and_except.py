# 60.	Exception handling (try/except/finally)

# In[5]:


num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
try:
    result = num1 / num2
    print(" The result is :", result)
except ZeroDivisionError:
    print(" Zerodevisionerror occured")
except ValueError:
    print("Value error ocuured")
finally:
    print("execution completed")
