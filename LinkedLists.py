# Linked lists are an ordered collection of objects.
'''
Each element of a linked list is called a node, and every node has two different fields:
    1. Data contains the value to be stored in the node.
    2. Next contains a reference to the next node on the list.
'''
# The first node is called the head, and it’s used as the starting point for any iteration through the list. 
# The last node must have its next reference pointing to 'None' to determine the end of the list.
'''
In Python, there’s a specific object in the collections module that you can use for linked lists called deque (pronounced “deck”), which stands for double-ended queue.
collections.deque uses an implementation of a linked list in which you can access, insert, or remove elements from the beginning or end of a list with 
constant O(1) performance.
'''

from collections import deque
'''
llist = deque("abcde")                          # Create and populate linked list
print("Original Linked List: " + str(llist))

llist.append("f")                               # Append the value 'f' at the last of linked list
print("\nAfter appending: " + str(llist))

llist.pop()                                     # Removing the last value from linked list
print("\nAfter removing: " + str(llist))

llist.appendleft("z")                           # Append the value 'z' to the left side
print("\nAppending to left side: " + str(llist))

llist.popleft()                                 # Removing the left most value from linked list
print("\nRemoving the left element: " + str(llist))
'''



''' Implementing Queues: FIFO - First In First Out '''
'''
queue = deque()

queue.append("Mary")        # 1
queue.append("John")        # 2
queue.append("Susan")       # 3

print(queue)

queue.popleft()

print(queue)
'''



''' Implementing Stacks: LIFO - Last In First Out '''
# Simulating a browser history

history = deque()

history.appendleft("https://realpython.com/")                               # 3
history.appendleft("https://realpython.com/pandas-read-write-files/")       # 2
history.appendleft("https://realpython.com/python-csv/")                    # 1

print(history)

history.popleft()

print(history)