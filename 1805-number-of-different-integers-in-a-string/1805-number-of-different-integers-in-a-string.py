import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        aset = set()
        value = ''
        i, j = 0, 0
        while i < len(word):
            if word[i].islower():
                i += 1
                continue
            j = i
            while j < len(word) and not word[j].islower():
                if word[i] == '0':
                    i += 1
                j += 1
            aset.add(word[i:j])
            i = j
        return len(aset)