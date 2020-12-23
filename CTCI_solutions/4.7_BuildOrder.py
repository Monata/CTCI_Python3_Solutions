# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second
# project is dependent on the first project). All of a project's dependencies must be built before the project is.
# Find a build order that will allow the projects to be built. If there is no valid build order, return an error.


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
        self.adj_nodes = set()

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


def build_order(project,order):
    traversed = []
    d = {}
    for val,key in order:
        d.setdefault(key,[]).append(val)
    d_right = {}
    for key,val in order:
        d_right.setdefault(key,[]).append(val)
    q = MyQueue()
    for i in project - set(d.keys()):
        q.push(i)
    while q:
        curr = q.pop()
        traversed.append(curr)
        for i in d_right.setdefault(curr,[]):
            if i in traversed:
                continue
            safe = True
            for v in d.setdefault(i,[]):
                if v not in traversed:
                    safe = False
                    break
            if safe:
                q.push(i)
    return traversed

if __name__ == "__main__":
    print("build_order")
    project = {'a','b','c','d','e','f'}
    order = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]

    print(build_order(project,order))