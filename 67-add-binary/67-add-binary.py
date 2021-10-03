class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Approach 2: Using bin() and int() built-int methods
        return str(bin(int(a,2) + int(b,2)))[2:]
        
        # Approach1: Brute-force
        remainder = ""
        i, j = (len(a) - 1, len(b) - 1)
        result = ""
        while i >= 0 and j >= 0:
            temp = remainder + a[i] + b[j]
            ptr = 0
            count = 0
            while ptr < len(temp):
                if temp[ptr] == "1":
                    count += 1
                ptr += 1
            
            if count == 3:
                result = "1" + result
                remainder = "1"
            elif count == 2:
                result = "0" + result
                remainder = "1"
            elif count == 1:
                result = "1" + result
                remainder = "0"
            else:
                result = "0" + result
            # print('result now ', result)
            i -= 1
            j -= 1
        
        while i >= 0:
            # print('a is bigger ', result, remainder)
            if remainder == "1":
                if a[i] == "1":
                   result = "0" + result
                   remainder = "1"
                else:
                    result = remainder + result
                    remainder = "0"
            else:
                result = a[i] + result
            
            i -= 1
        
        while j >= 0:
            if remainder == "1":
                if b[j] == "1":
                   result = "0" + result
                   remainder = "1"
                else:
                    result = remainder + result
                    remainder = "0"
            else:
                result = b[j] + result
            j -= 1
        
        if remainder == "1":
            return "1" + result
        
        return result
        