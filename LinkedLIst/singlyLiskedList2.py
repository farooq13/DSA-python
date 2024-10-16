class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertHead(self, newNode):
    temporaryNode = self.head
    self.head = newNode
    self.head.next = temporaryNode
    del temporaryNode

  def insertEnd(self, newNode):
    if self.head is None:
      self.head = newNode
    else:
      lastNode = self.head
      while lastNode.next:
        lastNode = lastNode.next
      lastNode.next = newNode
  
  def printList(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.data)
      currentNode = currentNode.next


firstNode = Node('Faruk')
secondNode = Node('Musa')
thirdNode = Node('Amin')

linkedList = LinkedList()
linkedList.insertEnd(firstNode)
linkedList.insertEnd(secondNode)
linkedList.insertHead(thirdNode)

linkedList.printList()