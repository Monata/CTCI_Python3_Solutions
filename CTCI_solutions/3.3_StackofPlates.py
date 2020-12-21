# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life,
# we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure
# SetOfStacks that mimics this. SetO-fStacks should be composed of several stacks and should create a new stack once
# the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single
# stack (that is, pop () should return the same values as it would if there were just a single stack).

class StackOfPlates:

    def __init__(self,lim):
        self.stacks = []
        self.limit = lim

    def push(self,item):
        if not self.stacks:
            self.stacks.append([])
        if len(self.stacks[-1]) < self.limit:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        if not self.stacks:
            return None
        if len(self.stacks[-1]) > 0:
            res = self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
            return res

    def popAt(self,stackNo):
        if stackNo < len(self.stacks):
            if len(self.stacks[stackNo]) > 0:
                return self.stacks[stackNo].pop()


if __name__ == "__main__":
    print("StackofPlates")
    l = StackOfPlates(30)
    for i in range(100):
        l.push(i)
    print(l.popAt(2))
    for i in range(1000):
        print(l.popAt(41))
    print(l.pop())
