class Solution:
    def convertToTitle(self, num: int) -> str:
        '''
        173659
        
        65-90
        
        '''
        # A = ord('A')
        # result = []
        # while columnNumber > 0:
        #     value = columnNumber % 10
        #     # print('val: ', value, A+value-1)
        #     result.append(chr(A+value-1))
        #     columnNumber //= 10
        # return "".join(result[::-1])
    
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)