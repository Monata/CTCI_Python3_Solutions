#create minimal height binary tree from given array
from bisect import bisect

class BinaryNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        t = ''
        if self.left and self.right:
            t += "(({})-{}-({}))".format(self.left,self.data,self.right)
        elif self.left:
            t += "(({})-{})".format(self.left,self.data)
        elif self.right:
            t += "({}-({}))".format(self.data,self.right)
        else:
            t += str(self.data)
        return t


def TreeConstructor(nodes):
    l = len(nodes)
    if l:
        current = BinaryNode(nodes[l//2])
        current.left = TreeConstructor(nodes[:l//2])
        current.right = TreeConstructor(nodes[l//2+1:])
        return current
    return None

if __name__ == "__main__":
    l = [i for i in range(0,15)]
    print("MinimalTree")
    tree = TreeConstructor(l)
    print(tree)


