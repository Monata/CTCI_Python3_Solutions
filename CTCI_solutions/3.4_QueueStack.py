# Implement a MyQueue class which implements a queue using two stacks


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


class MyQueue:

    def __init__(self):
        self.old_stack = MinStack()
        self.new_stack = MinStack()

    def push(self, item):
        self.new_stack.push(item)

    def pop(self):
        while self.new_stack.pointer != -1:
            self.old_stack.push(self.new_stack.pop())
        return self.old_stack.pop()

    def peek(self):
        while self.new_stack.pointer != -1:
            self.old_stack.push(self.new_stack.pop())
        return self.old_stack.peek()


if __name__ == "__main__":
    print("QueueStack")
    l = MyQueue()
    for i in range(0,10000,100):
        l.push(i)
    for i in range(0,10000,100):
        print(l.pop())