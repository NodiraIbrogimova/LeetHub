class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        h-index (f) = {max{i in :f(i) >= i}}
        '''
        count = [0]*(len(citations)+1)
        for c in citations:
            count[min(len(citations), c)] += 1
        i = len(citations)
        total = 0
        while i >= 0:
            total += count[i]
            if i <= total:
                return i
            i -= 1
        return 0