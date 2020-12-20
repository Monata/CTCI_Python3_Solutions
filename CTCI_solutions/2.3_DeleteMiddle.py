# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list,
# given only access to that node.

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


def delete_kth(head,k):
    runner = head.next
    while runner:
        runner = runner.next
        if runner:
            runner = runner.next
        else:
            break
        head = head.next
    head.next = head.next.next

if __name__ == "__main__":
    print("get_kth")
    ll = LinkedList()
    pt = ll
    for i in range(1,6):
        pt.next = Node(i)
        pt = pt.next
    pt = None
    print("initial", ll)
    delete_kth(ll,2)
    print("after",ll)
