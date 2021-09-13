class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {}
        for bill in bills:
            if bill == 10:
                hashmap[5] = hashmap.get(5, 0) - 1
            elif bill == 20:
                if hashmap.get(10):
                    hashmap[10] -= 1
                    hashmap[5] = hashmap.get(5, 0) - 1
                else:
                    hashmap[5] = hashmap.get(5, 0) - 3
            hashmap[bill] = hashmap.get(bill, 0) + 1
            if hashmap.get(5, -1) < 0:
                return False
        return True
        
        