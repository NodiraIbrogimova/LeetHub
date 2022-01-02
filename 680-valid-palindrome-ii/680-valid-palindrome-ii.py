class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if there's only one odd count char, the s can be palindrome
        # else, not a palindrome
        
        
#         # check if 
#         head, tail = 0, len(s)-1
#         while head < tail:
#             if s[head] != s[tail]:
                
#                 pass
#             head += 1
#             tail -= 1
        p1=0
        p2=len(s)-1
        while p1<=p2:
            if s[p1]!=s[p2]:
                string1=s[:p1]+s[p1+1:]
                string2=s[:p2]+s[p2+1:]
                return string1==string1[::-1] or string2==string2[::-1]
            p1+=1
            p2-=1
        return True