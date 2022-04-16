class MinStack:
    
    def __init__(self):
        self.deque = deque()
        self.mins = list()
        
        
    def push(self, val: int) -> None:
        self.deque.append(val)
        # For minimum stack https://www.youtube.com/watch?v=ufwPuyxkNVE
        if not self.mins:
            self.mins.append(val)
        elif self.mins[-1] >= val:
            self.mins.append(val)
        
        
    def pop(self) -> None:
        element = self.deque[-1]
        if element == self.mins[-1]:
            self.mins.pop()
        return self.deque.pop()

    
    def top(self) -> int:
        return self.deque[-1]

    
    def getMin(self) -> int:
        if self.mins: return self.mins[-1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()