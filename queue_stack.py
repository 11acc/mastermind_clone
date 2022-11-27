
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self): # Stack constructor. When we initialize the Stack, it is empty, so the top pointer is null (None)
    self.top = None
    self.stack_size = 0
    self.stack_list = []

  def push(self, value): # each value shall be "pushed" at the beginning of the linked list  
    node = Node(value) # Create a new Linked List Node
    node.next = self.top # Link the new node with the head of the list, this is, the top of the stack
    self.top = node # Make the new node become the top
    self.stack_list.append(node) # Add the node to the list
    self.stack_size += 1 # Increment the size of the stack
  
  def pop(self):
    if self.top is None: # Base case to avoid Stack Underflows
      return None
    node = self.top # get the node at the top
    self.top = node.next # make top point to the next element in the list
    self.stack_list.pop() # remove node from stack list
    self.stack_size -= 1 # decrease the size of the stack
    return node.value

class Queue:
  def __init__(self):  # When we initialize the Queue, it is empty, so head and tail pointers are null (None)
    self.head = None
    self.tail = None

  def enqueue(self, value):
    node = Node(value)  # Create a new linked list node to hold that value.
    if self.head is None:  # If the queue is empty (head is null (and so is tail)), make both head point to this new node
      self.head = node
    else:                  # Otherwise, add the node at the end of the list (after the current tail)
      self.tail.next = node
    self.tail = node  # Now readjust the tail to make it point to the newly inserted node

  def dequeue(self):
    if self.head is None:  # Base case to avoid Queue Underflows. If there are no elements, we simply return None
      return None
    node = self.head  # Extract the node at the head
    self.head = self.head.next  # Rearrange the head to point to the next element in the list.
    if self.head is None:  # If the new head is None it means the stack becomes empty after extracting the `node`, so make the tail also to point to None
      self.tail = None
    return node.value  # Return the extracted value