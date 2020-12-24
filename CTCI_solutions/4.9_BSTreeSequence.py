# DA binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

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
def sequences(node):
    res = []
    if node:
        right = sequences(node.right) # [[2]]
        left = sequences(node.left)  # [[0]]
        if left and right:
            for r in right:
                for l in left:
                    accum = []
                    weave(l,r,[],accum)
                    for i in accum:
                        i.insert(0,node.data)
                        res.append(i)
        elif right:
            for r in right:
                accum = []
                weave([], r, [], accum)
                for i in accum:
                    i.insert(0, node.data)
                    res.append(i)
        elif left:
            for l in left:
                accum = []
                weave(l, [], [], accum)
                for i in accum:
                    i.insert(0, node.data)
                    res.append(i)
        else:
            res.append([node.data])
    return res


if __name__ == "__main__":
    print("Sequences")
    l = [i for i in range(0, 8)]
    l1 = ['1','2']
    l2 = ['a','b']

    tree = TreeConstructor(l)
    ll_dict = {}
    print(tree)
    for i in sequences(tree):
        print(tree_iterative(i))
