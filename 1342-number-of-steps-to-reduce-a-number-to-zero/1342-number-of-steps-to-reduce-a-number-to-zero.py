class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        one = 0x00000001
        while num != 0:
            if num & one:
                # print('num 1: ', num)
                num ^= one
            else:
                # print('num 2: ', num)
                num >>= 1
            # print('num: ', num)
            count += 1
        return count
        