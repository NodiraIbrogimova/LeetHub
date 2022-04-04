class CustomStack:
    
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = deque()
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.appendleft(x)
        print('res: ', self.stack)

    def pop(self) -> int:
        if not self.stack:
            return -1
        element = self.stack[0]
        self.stack.popleft()
        return element

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(len(self.stack)-k, len(self.stack)):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)