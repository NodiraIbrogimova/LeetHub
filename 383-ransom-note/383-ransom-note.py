class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Warm-up
        letters = [0]*(26)
        a = ord('a')
        for letter in magazine:
            letters[ord(letter) - a] += 1
        for note in ransomNote:
            position = ord(note) - a
            if not letters[position]:
                return False
            letters[position] -= 1
        return True
        
        # Approach 3
        # Using one chararray
        # Time: O(n)
        # Space: O(1)
        # count = [0]*26
        # a = ord('a')
        # for achar in magazine:
        #     count[ord(achar)-a] += 1
        # for achar in ransomNote:
        #     count[ord(achar) - a] -= 1
        #     if count[ord(achar) - a] < 0:
        #         return False
        # return True
    
        # Approach 2
        # Similar to approach 1 but with chararray
        # ransom_count = [0]*26
        # magazine_count = [0]*26
        # a = ord('a')
        # for achar in ransomNote:
        #     ransom_count[ord(achar)-a] += 1
        # for achar in magazine:
        #     magazine_count[ord(achar)-a] += 1
        # for i in range(len(ransom_count)):
        #     if ransom_count[i] > 0 and ransom_count[i] > magazine_count[i]:
        #         return False
        # return True
        
        # Approach 1
        # Create a hashmap of chars for ransomNote and magazine
        # Check if all counts and values match
        # return True if yes, False otehrwise
        # Time: O(n)
        # Space: O(1) for two lowercase English letters hashmaps
        # ransom_hash, magazine_hash = {}, {}
        # for anote in ransomNote:
        #     ransom_hash[anote] = ransom_hash.get(anote, 0) + 1
        # for achar in magazine:
        #     magazine_hash[achar] = magazine_hash.get(achar, 0) + 1
        # for achar in ransom_hash:
        #     if achar not in magazine_hash or ransom_hash[achar] > magazine_hash[achar]:
        #         return False
        # return True
            
        