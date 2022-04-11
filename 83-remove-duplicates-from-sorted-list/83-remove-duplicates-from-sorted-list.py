# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr = head
        prev = curr
        while curr:
            prev = curr
            curr = curr.next
            while curr and prev.val == curr.val:
                curr = curr.next
            prev.next = curr
        return head
                
        
        
        # dummy = ListNode(-1)
        # new_head = dummy
        # prev = None
        # while head:
        #     if prev == head.val:
        #         print('prev and head.val: ', prev, head.val)
        #         head = head.next
        #         continue
        #     prev = head.val
        #     dummy.next = head
        #     dummy = dummy.next
        #     head = head.next
        # return new_head.next
            
            
            
            
        