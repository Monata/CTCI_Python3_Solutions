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

def palindrome(l1):
    # Suppose the digits are stored in forward order. Repeat the above problem.
    stack = []
    p = l1.next
    c = 0
    while p:
        stack.append(p.data)
        c+=1
        p = p.next
    if c % 2 == 0:
        return stack[:c//2][::-1] == stack[c//2::]
    else:
        return stack[:c//2][::-1] == stack[c//2 + 1:]

if __name__ == "__main__":
    print("Palindrome")
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    pt = l1
    for i in [9, 7, 9]:
        pt.next = Node(i)
        pt = pt.next
    pt = l2
    for i in [6, 8, 5]:
        pt.next = Node(i)
        pt = pt.next
    pt = l3
    for i in [1, 6, 6, 1]:
        pt.next = Node(i)
        pt = pt.next
    print("initial", l1, "///", l2, "///", l3)
    print(palindrome(l1),palindrome(l2),palindrome(l3))
