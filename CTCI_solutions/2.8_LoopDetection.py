# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop


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
        while pt.next and len(l) < 15:
            pt = pt.next
            l.append(str(pt))
        return " -> ".join(l)


def loop_start(l1):
    # Suppose the digits are stored in forward order. Repeat the above problem.
    p1 = l1.next
    p2 = l1.next
    # stacc = []
    while p2:
        # stacc.append(p1)
        p1 = p1.next
        p2 = p2.next
        if p2:
            p2 = p2.next
        else:
            return False
        if p1 == p2:
            return p2.next.next.next.next
            # while p1:
            #     if p1.next in stacc:
            #         return p1
            #     p1 = p1.next
            # return True
    return False

if __name__ == "__main__":
    print("LoopDetect")
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    p1 = l1
    for i in [9, 7, 9, 0, 0, 3, 1]:
        p1.next = Node(i)
        p1 = p1.next
        if i == 7:
            looey = p1
    p1.next = looey
    p2 = l2

    for i in [6, 8, 5, 3, 1]:
        p2.next = Node(i)
        p2 = p2.next
        if i == 6:
            looey = p2
    p2.next = looey
    p3 = l3
    for i in [1, 6, 6, 1]:
        p3.next = Node(i)
        p3 = p3.next
    print("initial", l1)
    print("initial", l2)
    print(loop_start(l1),loop_start(l2),loop_start(l3))
