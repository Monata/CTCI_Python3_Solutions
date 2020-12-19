# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list

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


def get_kth(head,k):
    runner = head
    for i in range(k):
        runner = runner.next
    while runner:
        head = head.next
        runner = runner.next
    return head

if __name__ == "__main__":
    print("get_kth")
    ll = LinkedList()
    pt = ll
    for i in range(10):
        pt.next = Node(i)
        pt = pt.next
    pt = None
    print("initial", ll)
    print(get_kth(ll,2))
