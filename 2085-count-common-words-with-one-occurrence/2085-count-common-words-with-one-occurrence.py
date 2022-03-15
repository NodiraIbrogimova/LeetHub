class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Approach 2
        # Using sungle hashmap
        hashmap = Counter(words1)
        for word in words2:
            if word in hashmap and hashmap[word] < 2:
                hashmap[word] -= 1
        count = 0
        for word in words2:
            if hashmap.get(word, -1) == 0:
                count += 1
        return count
        
        
        # Approach 1
        # Using two hashmaps
        hashmap1 = Counter(words1)
        hashmap2 = Counter(words2)
        count = 0
        for word in hashmap1:
            if hashmap1[word] == 1 and hashmap2.get(word) and hashmap2[word] == 1:
                count += 1
        return count