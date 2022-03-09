# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next
        if not head:
            return head
        
        prev, middle, anext = None, head, head.next
        
        while anext:
            if prev == middle.val or middle.val == anext.val:
                prev = middle.val
                middle.val = -200
            else:
                prev = middle.val
            middle = anext
            anext = anext.next
        if prev == middle.val:
            middle.val = -200
            prev = None
        curr = head
        while curr and curr.val == -200:
            curr = curr.next
        while curr:
            anext = curr
            while anext and anext.val == -200:
                anext = anext.next
            if anext:
                curr.val, anext.val = anext.val, curr.val
            else:
                break
            curr = curr.next
        curr = head
        prev = curr
        while curr:
            if curr.val == -200:
                prev.next = None
            prev = curr
            curr = curr.next
            
        return head