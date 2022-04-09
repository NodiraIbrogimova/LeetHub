# Approach 2
# Using doubly-linked list
class Node:
    
    def __init__(self, data=0, prev=None, anext=None):
        self.data = data
        self.prev = prev
        self.anext = anext
        
        
class MyQueue:
    
    def __init__(self):
        self.size = 0
        self.queue = None
        self.head = None
        self.tail = None


    def push(self, value):
        # add Node to tail, update tail
        node = Node(data=value, prev = self.tail)
        if self.size == 0:
            self.head = node
        else:
            self.tail.anext = node
        self.tail = node
        self.size += 1
    
    def pop(self):
        # get from head, update head and return value
        if self.size == 0: return None
        value = self.head.data
        next_node = self.head.anext
        if next_node:
            next_node.prev = None
        self.head = next_node
        self.size -= 1
        return value
    
    def peek(self):
        # get from head
        if self.size == 0: return None
        value = self.head.data
        return value
    
    def empty(self):
        return self.size == 0
    
# Approach 1
# Using built-in data structure deque
'''
from collections import deque
class MyQueue:

    def __init__(self):
        self.deque = deque()
        

    def push(self, x: int) -> None:
        self.deque.append(x)
        

    def pop(self) -> int:
        if len(self.deque):
            value = self.deque.popleft()
            return value
        return None
        

    def peek(self) -> int:
        if len(self.deque):
            return self.deque[0]
        return None
        

    def empty(self) -> bool:
        return not len(self.deque)
'''       


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()