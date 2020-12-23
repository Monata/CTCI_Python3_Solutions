# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing
# additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

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

def common_ancestor(node,target_1,target_2):
    def common_ancestor_helper(node,target_1,target_2,found_1=False,found_2=False):
        if node:
            t_1l, t_2l,t_1r,t_2r = [False]*4
            if node.left:
                t_1l,t_2l = common_ancestor_helper(node.left,target_1,target_2,found_1,found_2)
            if node.right:
                t_1r, t_2r = common_ancestor_helper(node.right,target_1,target_2,found_1,found_2)
            found_1 = t_1l or t_1r
            found_2 = t_2l or t_2r
            if node == target_1:
                found_1 = True
            if node == target_2:
                found_2 = True
            if found_1 == True and found_2 == True:
                return node,False
            return found_1,found_2

    res = common_ancestor_helper(node,target_1,target_2)
    return res[0]

if __name__ == "__main__":
    l = [i for i in range(0,7)]
    print("Common_ancestor")
    tree = TreeConstructor(l)
    ll_dict = {}
    print(tree,tree.left.right,tree.right.right)
    print(common_ancestor(tree,tree.left,tree.left.left))


