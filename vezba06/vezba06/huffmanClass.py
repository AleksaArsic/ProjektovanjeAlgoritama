class HuffData:

    def __init__(self, freq, char):
        self.freq = freq
        self.char = char

class huffNode:

    def __init__(self, left = None, right = None, parent = None, freq = None, data = None, ):
        self.left = left
        self.right = right
        self.parent = parent
        self.freq = freq
        self.char = data

