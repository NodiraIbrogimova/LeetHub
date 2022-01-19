# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # warm-up
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
    
    
        walker, runner = head, head
        has_cycle = False
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if runner == walker:
                entry = head
                while walker != entry:
                    walker = walker.next
                    entry = entry.next
                return entry
        return None
        
        
        '''
        [3,2,0,-4]
        1
        [1]
        -1
        [1, 2]
        0
        '''
        
        
        
        
        
        
        
        # if head == None:
        #     return None
        # slow = fast = head
        # has_cycle = False
        # while slow.next and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         break
        # else:
        #     return None
        # ptr = head
        # while ptr != slow:
        #     ptr = ptr.next
        #     slow = slow.next
        # return ptr