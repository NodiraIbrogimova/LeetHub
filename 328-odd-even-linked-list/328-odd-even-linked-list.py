# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 2
        # Using the Solution:
        # Put the odd nodes in a linked list and the even nodes in another. 
        # Then link the evenList to the tail of the oddList.
        if head is None:
            return head
        odd, even = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
        
        
        # Approach 1
        # Create dummy node for odd and even vals heads
        # for each index with odd val, append Node to odd head
        # same for even valued node
        if head is None:
            return None
        if head.next is None:
            return head
        
        curr = head
        dummy_odd = ListNode(-1)
        dummy_even = ListNode(-1)
        head_even = dummy_even
        head_odd = dummy_odd
        index = 1
        while curr:
            if index % 2:
                dummy_odd.next = ListNode(curr.val)
                dummy_odd = dummy_odd.next
            else:
                dummy_even.next = ListNode(curr.val)
                dummy_even = dummy_even.next
            index += 1
            curr = curr.next
        head_odd = head_odd.next
        head_even = head_even.next
        dummy_odd.next = head_even
        return head_odd