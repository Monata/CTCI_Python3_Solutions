# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node
# (by reference) as the jth node of the second linked list, then they are intersecting.


# Implement a function to check if a linked list is a palindrome

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
    def __init__(self):
        self.next = None

    def __str__(self):
        l = []
        pt = self
        while pt.next:
            pt = pt.next
            l.append(str(pt))
        return " -> ".join(l)

def intersect(l1,l2):
    # Suppose the digits are stored in forward order. Repeat the above problem.
    p1 = l1.next
    p2 = l2.next

    c1 = 0
    c2 = 0
    while p1:
        p1 = p1.next
        c1 += 1
    while p2:
        p2 = p2.next
        c2 += 1
    p1 = l1.next
    p2 = l2.next
    if c1 > c2:
        for i in range(c1 - c2):
            p1 = p1.next
    else:
        for i in range(c2 - c1):
            p2 = p2.next

    while p1:
        if p1 == p2:
            return p1
        else:
            p1 = p1.next
            p2 = p2.next

    return False
if __name__ == "__main__":
    print("Intersection")
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    p1 = l1
    for i in [9, 7, 9,0,0,3,1]:
        p1.next = Node(i)
        p1 = p1.next
    p2 = l2
    for i in [6, 8, 5,3,1]:
        p2.next = Node(i)
        p2 = p2.next
    p3 = l3
    for i in [1, 6, 6, 1]:
        p3.next = Node(i)
        p3 = p3.next
    p1.next = l3.next
    p2.next = l3.next
    print("initial", l1)
    print("initial", l2)
    print(intersect(l1,l2))
