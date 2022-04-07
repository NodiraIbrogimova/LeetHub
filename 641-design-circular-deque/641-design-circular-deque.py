class Node:
    # +4mins
    def __init__(self, anext=None, prev=None, val=0):
        self.anext = anext
        self.prev = prev
        self.val = val


class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.curr_size = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.capacity == self.curr_size: return False

        new_node = Node(val=value)
        new_node.anext = self.head

        if self.curr_size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.anext = self.head
            self.head = self.head.prev
        self.curr_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.capacity == self.curr_size: return False

        new_node = Node(val=value)
        new_node.prev = self.tail
        if self.curr_size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.anext = new_node
            new_node.prev = self.tail
            self.tail = self.tail.anext
        self.curr_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.curr_size == 0: return False
        
        self.head = self.head.anext
        if self.head is None:
            self.tail = None
        self.curr_size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.curr_size == 0: return False
        prev_node = self.tail.prev
        if prev_node is None:
            self.tail, self.head = None, None
        else:
            prev_node.anext = None
            self.tail = prev_node
        self.curr_size -= 1
        return True

    def getFront(self) -> int:
        if self.curr_size == 0: return -1
        return self.head.val

    def getRear(self) -> int:
        if self.curr_size == 0: return -1
        return self.tail.val

    def isFull(self) -> bool:
        return self.curr_size >= self.capacity

    def isEmpty(self) -> bool:
        if self.curr_size == 0: return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()