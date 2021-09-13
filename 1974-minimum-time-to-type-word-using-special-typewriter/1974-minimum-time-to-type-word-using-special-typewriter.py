class Solution:
    def minTimeToType(self, word: str) -> int:
        '''
        1. Check the ascii position of the char in string
        2. Check the difference between current position and aimed char position
            choose the one with less difference
            accumulate that difference to the diff
        3. type it (inc acc by 1)
        '''
        
        curr = ord('a')
        steps = 0
        for achar in word:
            typing = ord(achar)
            # 1. move forward = abs(curr - typing)
            # 2. move backward = 26 - abs(curr - typing)
            steps += min(abs(curr-typing), 26 - abs(curr - typing))
            curr = typing
        return steps + len(word)