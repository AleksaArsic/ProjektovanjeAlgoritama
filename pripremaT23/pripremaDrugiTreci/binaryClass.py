
class Data:

    def __init__(self, number, character):
        self.number = number
        self.character = character

class Node:

    def __init__(self, left = None, right = None, parent = None, data = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data

class Tree:

    def __init__(self, root):
        self.root = root
        self.nodeCount = 0