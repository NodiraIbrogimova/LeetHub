class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hashmap1 = Counter(words1)
        hashmap2 = Counter(words2)
        count = 0
        for word in hashmap1:
            if hashmap1[word] == 1 and hashmap2.get(word) and hashmap2[word] == 1:
                count += 1
        return count