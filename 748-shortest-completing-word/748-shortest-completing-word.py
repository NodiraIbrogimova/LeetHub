class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        chars = [0]*26
        a = ord('a')
        total = 0
        for elem in licensePlate:
            for achar in elem:
                achar = achar.lower()
                value = ord(achar)
                if 97 <= value <= 122:
                    chars[ord(achar)-a] += 1
                    total += 1
        length = 2**32-1
        result = -1
        for i, word in enumerate(words):
            if len(word) < total or len(word) >= length:
                continue
            curr_chars = deepcopy(chars)
            for index, achar in enumerate(word):
                curr_chars[ord(achar)-a] -= 1
            for count in curr_chars:
                if count > 0:
                    break
            else:
                if len(word) < length:
                    result = i
                    length = len(word)
        return words[result]
                
                
                