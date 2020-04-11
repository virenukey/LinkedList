class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class LinkedList():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def sizeOfLinkList(self):
        i = 0
        current = self.head
        while current is not None:
            i = i+1
            current = current.getNext()
        return i

    def addNodeFront(self, newData):
        temp = Node(newData)
        temp.setNext(self.head)
        self.head = temp

    def search(self, data):
        if self.head is None:
            return "Linked List is empty. No Nodes to search."

        current = self.head
        while current is not None:
            if current.getData() == data:
                return True
            else:
                current = current.getNext()

        return False

    def remove(self, data):
        if self.head is None:
            return "Linked List is empty. No Nodes to search."

        current = self.head
        if current.getData() == data:
            self.head = current.getNext()
            current = None
            return

        previous = None
        while current and current.getData() != data:
            previous = current
            current = current.getNext()

        if current == None:
            print "data {} is not present".format(data)
        else:
            previous.setNext(current.getNext())

    def addNodeLast(self, newData):
        temp = Node(newData)
        if self.head is None:
            self.head = temp
            return

        current = self.head

        while current.getNext() is not None:
            current = current.getNext()

        current.setNext(temp)

    def addNotAtPos(self, newData, pos):
        if pos == 0:
            self.addNodeFront(newData)
        elif pos > self.sizeOfLinkList():
            print "index out of range"
        elif pos == self.sizeOfLinkList():
            self.addNodeLast(newData)
        else:
            current = self.head
            i = 1
            while current is not None:
                if (i - pos) == 0:
                    break
                else:
                    current = current.getNext()
                    i = i+1
            temp = Node(newData)
            next = current.getNext()
            current.setNext(temp)
            temp.setNext(next)

    def removeDuplicates(self):
        current = self.head
        a = {}
        size = self.sizeOfLinkList()
        while size:
            if current.getData() in a:
                self.remove(current.getData())
            else:
                a[current.getData()] = None
            current = current.getNext()
            size = size - 1

    def reverseLinkedList(self):
        current = self.head
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        current = self.head
        while (current):
            print current.getData()
            current = current.getNext()








