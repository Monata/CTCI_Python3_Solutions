# Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an algorithm to determine if T2 is a
# subtree of Tl.

# DA binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
from random import shuffle


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
    def __init__(self, node=None):
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

    def add_node(self, node):
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
            t += "(({})-{}-({}))".format(self.left, self.data, self.right)
        elif self.left:
            t += "(({})-{})".format(self.left, self.data)
        elif self.right:
            t += "({}-({}))".format(self.data, self.right)
        else:
            t += str(self.data)
        return t


def TreeConstructor(nodes):
    l = len(nodes)
    if l:
        current = BinaryNode(nodes[l // 2])
        current.left = TreeConstructor(nodes[:l // 2])
        current.right = TreeConstructor(nodes[l // 2 + 1:])
        return current
    return None

def tree_iterative(nodes):
    if nodes:
        nodes.reverse()
        tree = BinaryNode(nodes[-1])
        nodes.pop()
    else:
        return None
    while nodes:
        curr = nodes[-1]
        nodes.pop()
        runner = tree
        while runner:
            if curr > runner.data:
                if runner.right:
                    runner = runner.right
                else:
                    runner.right = BinaryNode(curr)
                    break
            else:
                if runner.left:
                    runner = runner.left
                else:
                    runner.left = BinaryNode(curr)
                    break
    return tree

def weave(l1,l2,res,accum):
    if l1 and l2:
        weave(l1[1:],l2,res + [l1[0]],accum)
        weave(l1,l2[1:],res + [l2[0]],accum)
    elif l1:
        weave(l1[1:],l2,res + [l1[0]],accum)
    elif l2:
        weave(l1,l2[1:],res + [l2[0]],accum)
    else:
        accum.append(res)
# 1,2
# a,b,c
# 1 2

# a,1,b,2,c
# a,1,2,b,c
# 1,a,b,2,c
# 1,a,2,b,c
def sequences(node,target):
    if node:
        if node == target:
            if str(node) == str(target):
                return True
        else:
            return sequences(node.right,target) or sequences(node.left,target)
    return False

class BinaryTree:

    def __init__(self,root):
        self.root = root

    def helper_find(self,node, target):
        if node:
            if node.data == target:
                return node
            else:
                n1 = self.helper_find(node.right, target) or self.helper_find(node.left, target)
        return False

    def find(self,elem):
        return self.helper_find(self.root, elem)
if __name__ == "__main__":
    print("Check Subtree")
    l = [i for i in range(0,10000)]
    shuffle(l)
    l1 = ['1','2']
    l2 = ['a','b']
    tree = TreeConstructor(l)
    sub_tree = tree.left.right.right.right.right.left.left.left.right

    print(sub_tree)
    print(sequences(tree,sub_tree))
