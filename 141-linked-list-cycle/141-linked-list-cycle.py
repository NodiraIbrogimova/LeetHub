# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # warm-up
        # Imagine the scenario when person A runs with speed of x and B with double speed of A = 2x
        # If given road is 6points:
        # A makes 6steps
        # B makes 3 steps and at 6steps reaches A at time t, or makes another run of the whole road
        # This makes a decision that, whenever there is a cycle, B reaches A at some point as it moves 
        # twice the speed of A
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Approach 2 - repeated in learning Linked List card
        walker, runner = head, head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                entry = head
                while entry != walker:
                    entry = entry.next
                    walker = walker.next
                return entry
        return None
        
        
        # Approach 2:
        # After learning from Mudin and discussions:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
        
        # Approach 1:
        # Try counting the steps. If they exceed the max range provided in the description, return False
        slow, fast = head, head
        counter = 0
        while fast:
            if counter > 0 and counter % 2 == 0:
                slow = slow.next
            fast = fast.next
            counter += 1
            if slow == fast:
                print('returning counter: ', counter)
                return counter
            
        print('returning -1')
        return -1
        
        