# You are given a binary tree in which each node contains an integer value (which might be positive or negative).
# Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end
# at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

from collections import Counter
from random import randint


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


    def find_sum(self,target_sum):
        class num_counter:
            def __init__(self):
                self.count = 0

            def __iadd__(self, other):
                self.count += other
                return self

        count = num_counter()
        self.find_sum_helper(self.root,target_sum,count)
        return count.count

    def find_sum_helper(self, node, target_sum, count, path=None):
        if path is None:
            path = []
        if node:
            path.append(node.data)
            while sum(path) > target_sum:
                path.pop(0)

            if sum(path) == target_sum:
                print('->'.join([str(i) for i in path]))
                count += 1

            self.find_sum_helper(node.right,target_sum,count,path.copy())
            self.find_sum_helper(node.left,target_sum,count,path.copy())



    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    print("find_sum") ##positives
    t = BinaryTree([3])
    t.root = TreeConstructor(range(1000000))
    print(t)
    print(t.find_sum(1297))

