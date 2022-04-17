# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class Node:
    def __init__(self, key=None, next= None):
        self.key = key
        self.next = next
        
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = (10**6)+1
        self.hashset = [None for _ in range(self.size+1)]
    
    def _get_hash(self, key):
        accum, str_key = 0, str(key)
        for el in str_key:
            accum += ord(el)
        return accum % self.size
    
    def add(self, key: int) -> None:
        position = self._get_hash(key)
        head = self.hashset[position]
        if head is None: 
            self.hashset[position] = Node(key=key)
            return
        while head:
            if head.key == key:
                return
            head = head.next
        self.hashset[position] = Node(key=key, next=self.hashset[position])
            
        
    def remove(self, key: int) -> None:
        position = self._get_hash(key)
        head = self.hashset[position]
        if head is None:
            return
        if head.key == key:
            self.hashset[position] = self.hashset[position].next
            return
        prev = head
        head = head.next
        while head:
            if head.key == key:
                prev.next = head.next
                return
            prev = prev.next
            head = head.next
    
    def contains(self, key: int) -> bool:
        position = self._get_hash(key)
        head = self.hashset[position]
        while head:
            if head.key == key:
                return True
            head = head.next
        return False