class Solution:
    def isValid(self, s: str) -> bool:
        # Approach 2
        # Warm-up
        if not s: return False
        stack = list()
        closing_braces = {'(':')', '{': '}', '[': ']'}
        for i in range(len(s)):
            if stack and closing_braces.get(stack[-1]) == s[i]: stack.pop()
            else: stack.append(s[i])
        return len(stack) == 0
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Approach 1
        opening = {"(":0, "{":1, "[":2}
        closing = {")":3, "}":4, "]":5}
        stack = []
        if s[0] in opening:
            stack.append(opening[s[0]])
        else:
            stack.append(closing[s[0]])
        i = 1
        while i < len(s):
            if s[i] in opening:
                stack.append(opening[s[i]])
            else:
                stack.append(closing[s[i]])
            if len(stack) >> 1 and stack[-1] == (stack[-2] + 3):
                stack.pop(-1)
                stack.pop(-1)
            i += 1
        return len(stack) == 0
            
            
            