class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return x
        
        # Approach 2
        # Newton's formula for square root = .5*(n+(x//n))

        root = x
        while root*root > x:
            root = (root + x/root)// 2
        return int(root)
        
        
        # Approach 1
        # Add .1 each time and check if number's square becomes bigger or equal the number
        # Time: O(n)
        # Space: O(1)
        # Doesn't work :)
        squaredNums = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
        i = 1
        while i <= x//2:
            squared = i*i
            # print('squared: ', squared)
            if int(squared) >= x:
                # if int(squared) > x:
                #     print('\nsquared: ',squared)
                #     print('return i-.1 for x', x, i-0.1)
                #     return int(i - 0.1)
                print('return i for x', x, i)
                return int(i)
            i += 0.1
        print('return: ', i)
        return int(i)
    '''
    247776352
9
4
8
0
3
11
2147483647
    '''
        
        