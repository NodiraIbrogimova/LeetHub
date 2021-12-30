class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        smallest = 1
        remainder = smallest % k
        while remainder != 0:
            smallest = smallest*10 + 1
            remainder = smallest % k
            
        num_length = 0
        number = smallest
        while number > 0:
            number //= 10
            num_length += 1
        return num_length
    