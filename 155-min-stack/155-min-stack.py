# class Node:
    
#     def __init__(self, val=0, anext=None, prev=None):
#         self.val = val
#         self.anext = anext
#         self.prev = prev
        

class MinStack:

    def __init__(self):
        self.deque = deque()
        self.min_index = 0
        
    def push(self, val: int) -> None:
        self.deque.append(val)

    def pop(self) -> None:
        element = self.deque[-1]
        return self.deque.pop()

    
    def top(self) -> int:
        return self.deque[-1]

    
    def getMin(self) -> int:
        return min(self.deque)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()