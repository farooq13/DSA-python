# LinkedList 1 : inset at the end of a linkedList
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

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


firstNode = Node('John')
linkedList = LinkedList()
linkedList.insertEnd(firstNode)

secondNode = Node('Ben')
linkedList.insertEnd(secondNode)

thirdNode = Node('Robot')
linkedList.insertEnd(thirdNode)

linkedList.printList()