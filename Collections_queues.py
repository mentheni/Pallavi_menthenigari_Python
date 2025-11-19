#!/usr/bin/env python
# coding: utf-8

# 41.	Implement a stack using collections.deque

# In[1]:


from collections import deque

list1 = [10,20,30,40,50,60,70]

d = deque(list1)
d.append(80)
print(d)
d.appendleft(5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)




# In[14]:


from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    # Push element onto stack
    def push(self, item):
        self.stack.append(item)

    # Pop element from stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    # Peek at top element
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get stack size
    def size(self):
        return len(self.stack)

    # Print stack
    def display(self):
        return list(self.stack)
# Usage Example
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.display())
print("Top element:", s.peek())
print("Popped element:", s.pop())
print("Stack after pop:", s.display())
print("Is empty?", s.is_empty())


# 42.	Implement a queue using queue.Queue

# In[10]:


from queue import Queue

class MyQueue:
    def __init__(self):
        self.queue = Queue()
    def size(self):
        return self.queue.qsize()
    def enqueue(self, item):
        self.queue.put(item)

q = MyQueue()
q.enqueue(10)
q.enqueue(20)
print(q.size())





# In[3]:


from queue import Queue

class MyQueue:
    def __init__(self):
        self.queue = Queue()

    # Enqueue element
    def enqueue(self, item):
        self.queue.put(item)

    # Dequeue element
    def dequeue(self):
        if not self.is_empty():
            return self.queue.get()
        return "Queue is empty!"

    # Peek at the front element (not built-in, so we simulate it)
    def peek(self):
        if not self.is_empty():
            # Convert to list temporarily
            items = list(self.queue.queue)
            return items[0]
        return "Queue is empty!"

    # Check if queue is empty
    def is_empty(self):
        return self.queue.empty()

    # Get size of the queue
    def size(self):
        return self.queue.qsize()

    # Display queue contents
    def display(self):
        return list(self.queue.queue)


# In[4]:


q = MyQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:", q.display())
print("Front element:", q.peek())
print("Dequeued:", q.dequeue())
print("Queue after dequeue:", q.display())
print("Is empty?", q.is_empty())
print("Queue size:", q.size())


# 43.	Implement binary search tree (insert, search, traversal)

# In[ ]:





# 44.	Linked list implementation

# In[ ]:





# 45.	Factorial using recursion

# In[3]:


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

factorial(2)


# 46.	Fibonacci using recursion

# In[10]:


def febonacci(n):

    if n == 0:
        return 1
    elif n == 1 or n==2:
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)

n = 6
for i in range(n):
    print(febonacci(i))


# 47.	Tower of Hanoi problem

# In[12]:


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary)
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Example: 3 disks
tower_of_hanoi(3, 'A', 'B', 'C')


# In[ ]:




