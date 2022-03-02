class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        List: Qaysi ishlarni mazza qilib, holisona, hech kim majburlamasdan qilaman
        List: Qarama-qarshilik: Nimani haddan tashqari yomon ko'raman
        '''
        index=0 
        i=0
        while(i< len(t) and index<len(s)):
            if(t[i]==s[index]):
                index+=1
            i+=1        
        return index==len(s)