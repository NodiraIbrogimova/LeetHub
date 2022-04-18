class Node:
    
    def __init__(self, prev=None, data=0, anext=None):
        self.prev = prev
        self.data = data
        self.anext = anext


class Solution:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isValid(self, s: str) -> bool:
        # Approach 3
        # Using doubly-linked list
        if not s: return False
        closing_braces = {'(':')', '{': '}', '[': ']'}
        for achar in s:
            if self.head and closing_braces.get(self.head.data) == achar:
                self.head = self.head.prev
            else:
                new_node = Node(prev=self.head, data=achar)
                if self.head: 
                    self.head.anext = new_node
                self.head = new_node
        return self.head is None
                    
        
        # Approach 2
        # Warm-up
        # Using dynamic Python array as a stack DS
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