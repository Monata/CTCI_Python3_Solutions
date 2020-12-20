# Describe how you could use a single array to implement three stacks.


class ThreeStack:
    "used 0 as uninitialized"

    def __init__(self, size):
        from array import array
        self.array = array('d', [0] * size)
        self.length = size
        self.pointers = [-1, self.length, -1]

    def pop(self, stack_num):
        v = self.pointers[stack_num]
        if v != -1 and v != self.length:
            self.array[v] = 0
            if stack_num == 0:
                if (v % 3) != 1:
                    self.pointers[stack_num] -= 1
                else:
                    self.pointers[stack_num] -= 2
            elif stack_num == 1:
                if v + 1 < self.length:
                    if (v % 3) != 1:
                        self.pointers[stack_num] += 1
                    else:
                        if v + 2 < self.length:
                            self.pointers[stack_num] += 2
                        else:
                            self.pointers[stack_num] = -1
                else:
                    self.pointers[stack_num] = -1
            else:
                if v != 3:
                    self.pointers[stack_num] -= 3
                else:
                    self.pointers[stack_num] = -1

    def push(self, stack_num, num):
        v = self.pointers[stack_num]
        if stack_num == 0:
            while v + 1 < self.pointers[1]:
                if (v + 1) % 3 != 0:
                    self.array[v + 1] = num
                    self.pointers[stack_num] = v + 1
                    return None
                v += 1
        elif stack_num == 1:
            while v - 1 > self.pointers[0]:
                if (v - 1) % 3 != 0:
                    self.array[v - 1] = num
                    self.pointers[stack_num] = v - 1
                    return None
                v -= 1
        else:
            if v != -1:
                if v + 3 < self.length:
                    self.array[v + 3] = num
                    self.pointers[stack_num] = v + 3
            else:
                self.array[0] = num
                self.pointers[stack_num] = 3

    def peek(self, stack_num):
        v = self.pointers[stack_num]
        if v != -1 and v != self.length:
            return self.array[v]


if __name__ == "__main__":
    print("ThreeStack")
    l = ThreeStack(30)
    l.push(0,0)
    l.push(1,0)
    l.push(2,0)

