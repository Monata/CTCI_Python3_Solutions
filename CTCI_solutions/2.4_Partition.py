# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If xis contained within the list, the values of x only need to be after the elements less than x (see below).
# The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left
#                                                                                                   and right partitions


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


def partition(head,pivot):
    small_ll = LinkedList()
    sp = small_ll
    big_ll = LinkedList()
    bp = big_ll
    prev = head
    runner = head.next
    while runner:
        if runner.data < pivot:
            sp.next = runner
            prev = runner
            runner = runner.next
            sp = sp.next
            sp.next = None
            prev.next = None

        else:
            bp.next = runner
            prev = runner
            runner = runner.next
            bp = bp.next
            bp.next = None
            prev.next = None
    sp.next = big_ll.next
    head = small_ll
    return head

if __name__ == "__main__":
    print("partition")
    ll = LinkedList()
    pt = ll
    for i in [3,5,8,5,10,2,1]:
        pt.next = Node(i)
        pt = pt.next
    print("initial", ll)
    print(partition(ll,5))
