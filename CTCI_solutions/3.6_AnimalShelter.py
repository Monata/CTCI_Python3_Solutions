# : An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. People must
# adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they
# would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific
# animal they would like. Create the data structures to maintain this system and implement operations such as
# enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure


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

class ShelterQueue():
    def __init__(self):
        self.dog_stack = MyQueue()
        self.cat_stack = MyQueue()
        self.id = 0

    def enqueue(self, item):
        if item == 'dog':
            self.dog_stack.push((item,self.id))
            self.id += 1
        elif item == 'cat':
            self.cat_stack.push((item,self.id))
            self.id += 1

    def dequeue_any(self):
        if self.cat_stack and self.dog_stack:
            if self.cat_stack.peek()[1] < self.dog_stack.peek()[1]:
                return self.cat_stack.pop()
            else:
                return self.dog_stack.pop()
        elif self.cat_stack:
            return self.cat_stack.pop()
        elif self.dog_stack:
            return self.dog_stack.pop()

    def dequeue_cat(self):
        if self.cat_stack:
            return self.cat_stack.pop()

    def dequeue_dog(self):
        if self.dog_stack:
            return self.dog_stack.pop()



if __name__ == "__main__":
    print("ShelterQueue")
    l = ShelterQueue()
    for i in [0,9,2,7,4,8,-1]:
        l.enqueue('cat' if i  % 2 == 0 else 'dog')
    for i in range(0,10):
        print(l.dequeue_any())