class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first, second, third = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        result =  []
        for word in words:
            first_letter = word[0].lower()
            group = first
            if first_letter in second:
                group = second
            elif first_letter in third:
                group = third
            for letter in word:
                letter = letter.lower()
                if letter not in group:
                    break
            else:
                result.append(word)
                
        return result
                
        
        