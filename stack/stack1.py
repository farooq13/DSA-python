from collections import deque

stack = deque()

stack.append("https://www.risein.com/courses/blockchain-basics")
stack.append("https://www.risein.com/learn")
stack.append("https://www.risein.com/partner-with-us")


stack.pop()
stack.pop()
stack.pop()

print(stack)