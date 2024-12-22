from collections import deque


class Stack:
  def __init__(self):
    self.container = deque()

  def push(self, val):
    self.container.append(val)

  def pop(self):
    return self.container.pop()
  
  def peek(self):
    return self.container[-1]
  
  def is_empty(self):
    return len(self.container) == 0
  
  def size(self):
    return len(self.container)
  
  def __str__(self):
    return f"Stack: {list(self.container)}"
  

s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.peek()
print(s.peek())
s.pop()
print(s.peek())
