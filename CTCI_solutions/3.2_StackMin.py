# return min o(1)


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
            del self.stack[self.pointer]
            self.pointer -= 1

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


if __name__ == "__main__":
    print("MinStack")
    l = MinStack()
    l.push(0)
    l.push(-7)
    l.push(2)
    l.pop()
    print(l.min())
