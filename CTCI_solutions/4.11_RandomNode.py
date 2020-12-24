# You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method
# getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design
# and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods
from collections import Counter
from random import shuffle, randint


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


class BinaryTree:

    def __init__(self, l):
        self.length = len(l)
        self.root = tree_iterative(l)

    def helper_find(self, node, target):
        if node:
            if node.data == target:
                return node
            else:
                n1 = self.helper_find(node.right, target)
                if n1:
                    return n1
                n2 = self.helper_find(node.left, target)
                if n2:
                    return n2
        return False

    def find(self, elem):
        return self.helper_find(self.root, elem)

    def add(self, elem):
        new_node = False
        self.length += 1
        runner = self.root
        while runner:
            if elem > runner.data:
                if runner.right:
                    runner = runner.right
                else:
                    new_node = BinaryNode(elem)
                    runner.right = new_node
                    break
            else:
                if runner.left:
                    runner = runner.left
                else:
                    new_node = BinaryNode(elem)
                    runner.left = new_node
                    break
        return new_node

    def helper(self, node, count):
        if node:
            count -= 1
            if count == 0:
                return node
            res = self.helper(node.left, count)
            if isinstance(res, int):
                res = self.helper(node.right, res)
            return res
        return count

    def get_random_node(self):
        till = randint(1, self.length)
        return self.helper(self.root, till)

    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    print("RandNode")
    l = [5,4,1,2,0,6]
    test_count = Counter(l + [3])
    t = BinaryTree([3])
    for i in l:
        t.add(i)
    for i in range(len(test_count.values()) * 1000):
        test_count[t.get_random_node().data] += 1
    print(test_count)

