class Solution:
    def checkForLower(self, start, to, word):
        for i in range(1, len(word)):
            if start <= ord(word[i]) <= to:
                return False
        return True
    
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        # check if the first letter is capital
        # if so, the rest should be either all capital either all lowercase
        first_isUpper = (ord('A') <= ord(word[0]) <= ord('Z'))
        second_isUpper = (ord('A') <= ord(word[1]) <= ord('Z'))
        
        if first_isUpper and second_isUpper:
            start, to = ord('a'), ord('z')
        else:
            start, to = ord('A'), ord('Z')
            
        return self.checkForLower(start, to, word)
        
                
        