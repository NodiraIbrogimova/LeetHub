# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 3
        # Two pointers
        '''
        When should I delete/bypass a node:
            When these values are present more than once in the list
            How to detect if particular value is repetead?
        Notes:
            Repetitions can be present in the beginning, middle and in the end of the ll
            Make sure to cover all possibilities
            
        '''
        # Approach 4: Warm-up
        sentinel = ListNode(0, head)
        predecessor = sentinel
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                predecessor.next = head.next
            else:
                predecessor = predecessor.next
            head = head.next
        return sentinel.next
        
        
        # Approach 3: Warm-up
        # Time: O(n)
        # Space: O(100) = O(1)
        hashmap = dict()
        curr = head
        while curr:
            hashmap[curr.val] = hashmap.get(curr.val, 0) + 1
            curr = curr.next
        curr = head
        sentinel = ListNode()
        pred = sentinel
        while curr:
            if hashmap[curr.val] == 1:
                pred.next = curr
                pred = pred.next
            curr = curr.next
        pred.next = None
        return sentinel.next
        
    
        # Approach 2
        # Using hashset
        # TC: O(n), SC: O(1)
        if head is None: return head
        
        curr, seen, repeated = head, set(), set()
        while curr:
            if curr.val not in repeated:
                if curr.val not in seen: seen.add(curr.val)
                else: repeated.add(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.val in repeated: curr.val = None
            curr = curr.next
        
        curr, dummy_head = head, ListNode()
        dummy = dummy_head
        while curr:
            if curr.val:
                dummy.next = curr
                dummy = dummy.next
            curr = curr.next
        dummy.next = None
        return dummy_head.next
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Approach 1
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