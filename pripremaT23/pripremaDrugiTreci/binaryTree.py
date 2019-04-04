
def inorderTreeWalk(x):
    if x != None:
        inorderTreeWalk(x.left)
        print(x.data.number)
        inorderTreeWalk(x.right)

def treeInsert(T, z):
    
    T.nodeCount += 1
    
    y = None
    x = T.root

    while x != None:
        y = x
        if z.data.number < x.data.number:
            x = x.left
        else:
            x = x.right

    z.parent = y

    if y == None:
        T.root = z
    elif z.data.number < y.data.number:
        y.left = z
    else:
        y.right = z


def treeDelete(T, z):

    T.nodeCount -= 1

    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = treeMinimum(z.right)

        if y.parent != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y

        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y


def transplant(T, u, v):
    if u.parent == None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v != None:
        v.parent = u.parent

def treeMinimum(x):
    while x.left != None:
        x = x.left
    return x

def treeMaximum(x):
    while x.right != None:
        x= x.right
    return x

def treeSuccessor(x):
    
    if x.right != None:
        return treeMinimum(x.right)
    y = x.parent

    while y != None and x == y.right:
        x = y
        y = y.parent

    return y