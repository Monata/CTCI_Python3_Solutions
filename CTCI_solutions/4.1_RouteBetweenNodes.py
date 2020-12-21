# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two
# nodes.
class MinStack:
    def __init__(self):
        from array import array
        self.stack = []
        self.pointer = -1
        self.mindex = []
        self.minptr = -1

    def pop(self):
        if self.pointer != -1:
            if self.pointer == self.mindex[self.minptr]:
                self.mindex.pop()
                self.minptr -= 1
            res = self.stack[self.pointer]
            self.stack.pop()
            self.pointer -= 1
            return res

    def push(self, item):
        self.stack.append(item)
        self.pointer += 1
        if self.minptr != -1:
            if item < self.stack[self.mindex[self.minptr]]:
                self.mindex.append(self.pointer)
                self.minptr += 1
        else:
            self.mindex.append(self.pointer)
            self.minptr += 1

    def min(self):
        if self.minptr != -1:
            return self.stack[self.mindex[self.minptr]]

    def peek(self):
        if self.pointer != -1:
            return self.stack[self.pointer]

    def __bool__(self):
        return self.pointer != -1


class MyQueue:

    def __init__(self):
        self.old_stack = MinStack()
        self.new_stack = MinStack()

    def push(self, item):
        self.new_stack.push(item)

    def pop(self):
        while self.new_stack:
            self.old_stack.push(self.new_stack.pop())
        return self.old_stack.pop()

    def peek(self):
        while self.new_stack:
            self.old_stack.push(self.new_stack.pop())
        return self.old_stack.peek()

    def __bool__(self):
        return bool(self.new_stack or self.old_stack)

class Graph:
    nodes = []

    def __str__(self):
        return "\n".join([str(i) for i in self.nodes])

    def __getitem__(self, item):
        return self.nodes[item]


class Node:

    def __init__(self,data):
        self.data = data
        self.adj_nodes = []

    def __str__(self):
        return ("({}) -> {}".format(self.data,self.adj_nodes))

    def __repr__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

def breadth_first_search(start,target):
    queue = MyQueue()
    queue.push(start)
    visited = set()
    while queue:
        curr = queue.pop()
        visited.add(curr)
        if curr == target:
            return True
        else:
            for node in curr.adj_nodes:
                if node not in visited:
                    queue.push(node)
    return False
if __name__ == "__main__":
    print("RouteBetweenNodes")
    l = Graph()
    for i in range(100000):
        new_node = Node(i)
        if i != 0:
            l.nodes[-1].adj_nodes.append(new_node)
        if i % 3 == 0:
            for i in range(i//2,i,1000):
                i -= 2
                new_node.adj_nodes.append(l.nodes[i])
        l.nodes.append(new_node)
    print("initial //",l,"//")
    print(breadth_first_search(l[999],l[1]))