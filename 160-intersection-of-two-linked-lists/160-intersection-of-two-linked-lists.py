# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n, m = 0, 0 
        currA, currB = headA, headB
        while currA:
            n += 1
            currA = currA.next
        while currB:
            m += 1
            currB = currB.next
        if (n - m) < 0:
            # m is bigger
            bigHead = headB
            smallHead = headA
        #   n, m = m, n
        else:
            # n is bigger or equal
            bigHead = headA
            smallHead = headB
        diff = abs(n - m)
        while diff > 0:
            bigHead = bigHead.next
            diff -= 1
        while bigHead:
            if bigHead == smallHead:
                return bigHead
            bigHead = bigHead.next
            smallHead = smallHead.next
        return None
        