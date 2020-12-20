# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.

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


def sum_lists(l1, l2):
    p1 = l1.next
    p2 = l2.next
    res_list = LinkedList()
    resp = res_list
    rem = 0
    while p1 and p2:
        v = (p1.data + p2.data) + rem
        rem = v // 10
        resp.next = Node(v % 10)
        resp = resp.next
        p1 = p1.next
        p2 = p2.next
    while p1:
        v = p1.data + rem
        rem = v // 10
        resp.next = Node(v % 10)
        resp = resp.next
        p1 = p1.next
    while p2:
        v = p2.data + rem
        rem = v // 10
        resp.next = Node(v % 10)
        resp = resp.next
        p2 = p2.next
    if rem:
        resp.next = Node(rem)

    return res_list


def sum_lists_follow_up(l1, l2):
    # Suppose the digits are stored in forward order. Repeat the above problem.
    p1 = l1.next
    p2 = l2.next
    res_list = LinkedList()
    resp = res_list
    s1 = 0
    s2 = 0
    while p1:
        s1 = p1.data + s1*10
        p1 = p1.next
    while p2:
        s2 = p2.data + s2*10
        p2 = p2.next
    v = s1 + s2
    for i in str(v):
        resp.next = Node(int(i))
        resp = resp.next
    return res_list


if __name__ == "__main__":
    print("SumLists")
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    pt = l1
    for i in [9, 7, 8]:
        pt.next = Node(i)
        pt = pt.next
    pt = l2
    for i in [6, 8, 5]:
        pt.next = Node(i)
        pt = pt.next
    pt = l3
    for i in [1, 1, 6, 1]:
        pt.next = Node(i)
        pt = pt.next
    print("initial", l1, "///", l2, "///", l3)
    print(sum_lists_follow_up(l2, l1), sum_lists(l2, l3))
