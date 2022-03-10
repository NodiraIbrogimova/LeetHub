# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1, curr2 = l1, l2
        carry = 0
        while curr1 and curr2:
            asum = curr1.val + curr2.val + carry
            digit = asum % 10
            curr1.val = digit
            carry = asum // 10
            prev1 = curr1
            prev2 = curr2
            curr1 = curr1.next
            curr2 = curr2.next
            
        if curr2:
            prev1.next = curr2
            curr1 = prev1.next
        
        while curr1 and carry:
            asum = curr1.val + carry
            digit = asum % 10
            carry = asum // 10
            curr1.val = digit
            prev1 = curr1
            curr1 = curr1.next
            
        if carry:
            prev1.next = ListNode(carry, None)
        return l1