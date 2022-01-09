class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Approach 2
        # Warm-up
        # reverse [head+1:~head]
        # and
        # reverse [head:~head-1]
        # check if any match and return result
        s = list(s)
        head, middle = 0, len(s)//2
        while head < middle:
            if s[head] != s[~head]:
                right = s[head+1:len(s)-head]
                left = s[head:~head]
                return (len(right) > 0 and right == right[::-1]) or (len(left) > 0 and left == left[::-1])
            head += 1
        return True
            
        # Approach 1
        # from discussion
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