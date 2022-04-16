class MyHashMap:

    def __init__(self):
        self.size = (10**4)+1
        self.hashmap = [None for _ in range(self.size)]
    
    def _get_hash(self, key):
        result = 0
        str_key = str(key)
        for achar in str_key:
            result += ord(achar)
        return result % self.size
        
        
    def put(self, key: int, value: int) -> None:
        item = [key, value]
        ahash = self._get_hash(key)
        if not self.hashmap[ahash]:
            self.hashmap[ahash] = list([item])
        else:
            for pair in self.hashmap[ahash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.hashmap[ahash].append(item)
            return True
        
        
    def get(self, key: int) -> int:
        ahash = self._get_hash(key)
        if self.hashmap[ahash]:
            for pair in self.hashmap[ahash]:
                if pair[0] == key:
                    return pair[1]
        return -1
        
        
        
    def remove(self, key: int) -> None:
        ahash = self._get_hash(key)
        if not self.hashmap[ahash]: return False
        for index, pair in enumerate(self.hashmap[ahash]):
            if pair[0] == key:
                self.hashmap[ahash].pop(index)
                return True
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)