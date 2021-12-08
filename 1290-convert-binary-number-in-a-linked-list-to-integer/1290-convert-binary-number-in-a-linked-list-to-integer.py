# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        '''
        mask = 1 << p
        return (n & ~mask) | ((b << p) & mask)
        
        Given a number n, a position p and a binary value b, we need to change the         bit at position p in n to value b.
        '''
        curr = head
        if curr is None:
            return curr
        
        position = 0
        value = curr.val
        while curr.next:
            value = (value << 1) | curr.next.val
            curr = curr.next
        return value
        
        
        mask =  1 << 4
        print('mask: ', mask)
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num
        