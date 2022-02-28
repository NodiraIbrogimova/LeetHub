class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        A = ord('A')
        
        A...Z = 1...26
        AA...AZ = 27...52
        BA...BZ = 53...78
        CA....CZ = 79...104
        53 = 2,1 = [2//53 <= 2] chr(2%26**2 + A - 1)  +  [53//26 <= 53] chr(53%26**1+A-1)
        54 = 2,2 = [2//54 <= 2] chr(2%26**2 + A - 1)  +  [54//26 <= 54] chr(54%26**1+A-1)
        55 = 2,3
        ...
        78 =  1,26
        104 = 3,26
        703 = 1,1,1 = (703%26**1+A)
        '''
        A = ord('A')
        result = list()
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber%26 + A))
            columnNumber //= 26
        return "".join(result[::-1])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        result = list()
        A = ord('A')
        remainder = 0
        while remainder > 0:
            remainder = columnNumber%26
            result.append(chr(A + remainder - 1))
            columnNumber -= remainder
        if columnNumber >= 26:
            result.append(chr(A + columnNumber%26 - 1))
        return "".join(result)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        print('res: ', 701//26, 701%26)
        A = ord('A')
        result = []
        
        while columnNumber > 0:
            value = columnNumber // 26 + A
            print('value: ', value)
            result.append(chr(value))
            print('columnNumber: ', columnNumber)
            columnNumber %= 26
        return "".join(result[::-1])