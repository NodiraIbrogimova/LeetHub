class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        # the allowed word can be treated as a set of chars
        # as chars in allowed are distinct
        # but, for O(1) checking if the char is present in allowed, we make allowed set
        allowed = set(allowed)
        for word in words:
            unconsistent = 1
            for achar in word:
                if achar not in allowed:
                    unconsistent = 0
            
            count += unconsistent
        return count
        