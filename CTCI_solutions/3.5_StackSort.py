# Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary
# stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the
# following operations: push, pop, peek, and isEmpty.

class MinStack:
    def __init__(self):
        from array import array
        self.stack = array('d')
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

class SortedStack:

    def __init__(self):
        self.stack = MinStack()
        self.temp_stack = MinStack()

    def push(self,item):
        pushed = False
        while self.stack:
            if item > self.stack.peek():
                self.temp_stack.push(self.stack.pop())
            else:
                self.stack.push(item)
                pushed = True
                break
        if not pushed:
            self.stack.push(item)
        while self.temp_stack:
            self.stack.push(self.temp_stack.pop())

    def pop(self):
        return self.stack.pop()

    def isempty(self):
        return False if self.stack else True




if __name__ == "__main__":
    print("SortedStack")
    l = SortedStack()
    for i in [0,9,2,7,4,8,-1]:
        l.push(i)
    for i in range(0,10):
        print(l.isempty(),l.pop())