# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is
# defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.



class Node:
    "A simple linked list implementation"

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return "({})".format(self.data)


class LinkedList:
    def __init__(self,node = None):
        self.next = node

    def __str__(self):
        l = []
        pt = self
        while pt.next:
            pt = pt.next
            l.append(str(pt))
        return " -> ".join(l)

    def __repr__(self):
        return str(self)

    def add_node(self,node):
        pt = self
        while pt.next:
            pt = pt.next
        pt.next = node



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


def is_balanced_length(node):
    if node:
        left = is_balanced_length(node.left)
        right = is_balanced_length(node.right)
        if abs(left - right) < 2:
            return left + right + 1
        else:
            return -2
    else:
        return 0

def is_balanced(node):
    return is_balanced_length(node) > 0

if __name__ == "__main__":
    print("CheckBalanced")
    bad_tree = BinaryNode(0)
    pt = bad_tree
    for i in range(1,10):
        pt.right = BinaryNode(i)
        pt = pt.right

    for i in range(100):
        tree = TreeConstructor([i for i in range(i)]) # it builds balanced trees
        res = is_balanced(tree)
        if not res:
            print(tree)

    print(is_balanced(bad_tree),bad_tree)


