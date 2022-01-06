class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        amax = count = 0
        for sentence in sentences:
            spaces = 0
            for achar in sentence:
                if achar == ' ':
                    spaces += 1
            amax = max(spaces+1, amax)
        return amax
        