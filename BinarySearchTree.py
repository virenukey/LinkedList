class Node(object):

    def __init__(self, node=None):
        self.node = node
        self.right = None
        self.left = None

    def insert(self, value):
        if self.node == value:
            return False
        elif value < self.node:
            if self.left:
                self.left.insert(value)
                return True
            else:
                self.left = Node(value)
                return True
        else:
            if self.right:
                self.right.insert(value)
                return True
            else:
                self.right = Node(value)
                return True

    def find(self, value):
        if self.node == value:
            return True
        elif value < self.node and self.left:
            return self.left.find(value)
        elif value > self.right and self.right:
            return self.right.find(value)

        return False


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False

node = BST()
a = node.insert(10)
b = node.insert(9)
c = node.insert(10)
d = node.insert(8)
e = node.find(12)
print e



