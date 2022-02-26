class Solution:
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1
    
        if not n%2 or not n%3 or not n%5:
            return True
        return False
        
        
        BIN_TWO, BIN_THREE, BIN_FIVE = 0b10, 0b11, 0b110
        print(f'test: {n & BIN_TWO} or {n & BIN_THREE} or {n & BIN_FIVE}')
        if not (n & BIN_TWO) or not (n & BIN_THREE) or not (n & BIN_FIVE):
            return True
        return False