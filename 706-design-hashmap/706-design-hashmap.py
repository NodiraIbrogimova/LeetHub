class Node:

    def __init__(self, key=None, val=None, anext=None):
        self.key = key
        self.val = val
        self.next = anext


class MyHashMap:

    def __init__(self):
        self.size = (10 ** 4) + 1
        self.hashmap = [None for _ in range(self.size)]

    def _get_hash(self, key):
        accum = 0
        str_key = str(key)
        for achar in str_key:
            accum += ord(achar)
        return accum % self.size
    
    def put(self, key: int, value: int) -> None:
        position = self._get_hash(key)
        head = self.hashmap[position]
        if head is None:
            self.hashmap[position] = Node(key=key, val=value)
        else:
            while head:
                if head.key == key:
                    head.val = value
                    return True
                head = head.next
            self.hashmap[position] = Node(key=key, val=value, anext=self.hashmap[position])

    def get(self, key: int) -> int:
        position = self._get_hash(key)
        head = self.hashmap[position]
        if head:
            curr = head
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        position = self._get_hash(key)
        head = self.hashmap[position]
        
        if not head: return False
        if head.key == key:
            self.hashmap[position] = head.next
            return
        prev = head
        head = head.next
        while head:
            if head.key == key:
                prev.next = head.next
                return
            prev = prev.next
            head = head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)