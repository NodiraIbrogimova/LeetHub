class Solution:
    def replaceWithPrev(self, result, code, k):
        i = len(code)-1
        while i >= 0:
            keys = k
            j = i - 1
            asum = 0
            while keys < 0:
                asum += code[j % len(code)]
                j -= 1
                keys += 1
            result[i] = asum
            i -= 1
        return result

    def replaceWithNext(self, result, code, k):
        i = 0
        while i < len(code):
            # print('i', i)
            keys = k
            asum = 0
            j = i + 1
            while keys > 0: # 2
                # print('k', keys)
                asum += code[j % len(code)]
                keys -= 1
                j += 1
            result[i] = asum
            i += 1
        return result
        
    def replaceWithZero(self):
        pass

    def decrypt(self, code, k):
        result = [0]*len(code)
        if k > 0:
            return Solution().replaceWithNext(result, code, k)
        elif k < 0:
            return Solution().replaceWithPrev(result, code, k)
        else:
            return result