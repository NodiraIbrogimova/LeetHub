class Solution:
    def reverseBits(self, nums: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            if (nums & 1) == 1:
                result ^= 1
            nums >>= 1
        return result

            
            
        
        