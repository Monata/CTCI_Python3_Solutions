# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You
# may assume that each node has a link to its parent.


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

def successor(node,target,found = False):
    if node:
        if node.left:
            found = successor(node.left,target,found)
        if found == -1:
            return node
        if node == target:
            found = -1
        if node.right:
            found = successor(node.right, target, found)
        return found


if __name__ == "__main__":
    l = [i for i in range(0,7)]
    print("Successor")
    tree = TreeConstructor(l)
    ll_dict = {}
    print(successor(tree,tree.right.right))


