class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = [0]*26
        count_s2 = [0]*26
        a = ord('a')
        for achar in s1:
            count_s1[ord(achar)-a] += 1
        for i in range(len(s1)):
            count_s2[ord(s2[i])-a]+= 1
        if count_s1 == count_s2:
            return True
        i = 1
        while i+len(s1)-1 < len(s2):
            count_s2[ord(s2[i-1]) - a] -= 1
            count_s2[ord(s2[i+len(s1)-1]) - a] += 1
            if count_s1 == count_s2:
                return True
            i += 1
        return False
            