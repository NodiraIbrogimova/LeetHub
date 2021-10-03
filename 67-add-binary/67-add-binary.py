class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Approach 4: Optimize the time complexity for creating result str
        # It takes O(n^2) for creating such index. Aim is to reduce it to O(n) with storing str chars in a list and resturen the join version
        amax = max(len(a), len(b))
        a = a.zfill(amax)
        b = b.zfill(amax)
        carry, itr, result = (0, amax-1, [""]*(amax+1))
        
        while itr >=0 :
            counter = carry
            if a[itr] == '1':
                counter += 1
            if b[itr] == '1':
                counter += 1
            result[itr+1] = '0' if counter % 2 == 0 else '1'
            
            if counter < 2:
                carry = 0
            else:
                carry = 1
                
            itr -= 1
        if carry > 0:
            result[0] = '1'
        return "".join(result)
        
        
        # Approach 3: Optimize the naive (brute-force) solution in Approach 1
        # Learned hints from geeksforgeeks
        
        '''
        11011
          101
         
        3(10) => 011(2)
        2(10) => 010(2) .
        1(10) => 001(2)
        0(10) => 000(2) .
        '''
        amax = max(len(a), len(b))
        a = a.zfill(amax)
        b = b.zfill(amax)
        carry = 0
        result = ""
        itr = amax - 1
        while itr >= 0:
            counter = carry
            if b[itr] == '1':
                counter += 1
            if a[itr] == '1':                    
                counter += 1
            result = ('0' if counter % 2 == 0 else '1') + result
            carry = 0 if counter < 2 else 1
            itr -= 1
        if carry > 0:
            result = "1" + result
        return result
        
        
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
        