# Approach 2
# Using doublylinked list
class Node:

    def __init__(self, val=0, anext=None, prev=None):
        self.val = val
        self.anext = anext
        self.prev = prev


class CustomStack:

    def __init__(self, maxSize):
        self.capacity = maxSize
        self.curr_size = 0
        self.head = None
        self.tail = None

    def push(self, value):
        if self.curr_size == self.capacity: return -1
        new_node = Node(val=value)
        prev_node = self.head
        if self.curr_size == 0:  # or self.curr_size == 0
            self.tail = new_node
        else:
            new_node.anext = prev_node
            prev_node.prev = new_node
        self.head = new_node
        self.curr_size += 1

    def pop(self):
        if self.curr_size == 0: return -1
        value = self.head.val
        prev_node = self.head.anext
        if prev_node:
            prev_node.prev = None
            self.head.anext = None
        self.head = prev_node
        self.curr_size -= 1
        return value

    def increment(self, k, value):
        # inc k number of elements in the bottom by val
        curr = self.tail
        while curr and k:
            curr.val += value
            k -= 1
            curr = curr.prev

# Approach 1
# Using built-in data structure - deque
'''
class CustomStack:
    
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = deque()
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.appendleft(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        element = self.stack[0]
        self.stack.popleft()
        return element
    
                
    def increment(self, k: int, val: int) -> None:
        increment_range = min(k, len(self.stack))
        for i in range(len(self.stack)-increment_range, len(self.stack)):
            self.stack[i] += val
            
'''
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)