# Remove Dups! Write code to remove duplicates from an unsorted linked list.

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


def remove_dups(head):
    prev = head
    while prev.next:
        c2 = prev.next
        while c2.next:
            if c2.next.data == prev.next.data:
                prev.next = prev.next.next
                c2.next = c2.next.next
            else:
                c2 = c2.next
        prev = prev.next


if __name__ == "__main__":
    ll = LinkedList()
    pt = ll
    for i in range(10):
        pt.next = Node(i)
        pt = pt.next
    for i in range(3):
        pt.next = Node(i)
        pt = pt.next
    for i in range(7, 9):
        pt.next = Node(i)
        pt = pt.next
    pt = None
    print("initial", ll)
    remove_dups(ll)
    print("after", ll)
