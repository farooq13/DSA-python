class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, newNode):
    if self.head is None:
      self.head = newNode
    else:
      lastNode = self.head
      while lastNode.next:
        lastNode = lastNode.next
      lastNode.next = newNode

  def printList(self):
    if self.head is None:
      print('The list is empty')
      return
    currentNode = self.head
    while currentNode:
      print(currentNode.data)
      currentNode = currentNode.next


firstNode = Node('Faruk')
linkedList = LinkedList()
# linkedList.insert(firstNode)

secondNode = Node('Idris')
# linkedList.insert(secondNode)

thirdNode = Node('Abdulkadir')
# linkedList.insert(thirdNode)

linkedList.printList()