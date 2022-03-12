"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        # Approach 2: From Discussion
        # 1. Iterate the original list and duplicate each node. The duplicate
        # of each node follows its original immediately.
        # 2. Iterate the new list and assign the random pointer for each
        # duplicated node.
        # 3. Restore the original list and extract the duplicated nodes.
        curr = head
        while curr:
            new_node = Node(curr.val)
            anext = curr.next
            curr.next = new_node
            new_node.next = anext
            curr = anext
        curr = head
        while curr:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        deep_head = Node(-1)
        curr_deep = deep_head
        while curr:
            curr_deep.next = curr.next
            curr_deep = curr.next
            curr = curr.next.next
        curr = deep_head
        return deep_head.next
        # Time: O(n)
        # Space: O(n) [for storing pointer of random from node to node] + O(n) [for storing addresses and indices of original llist] + O(n) [for storing addresses and indices of new llist] + O(n) [for new llist] = O(n)
        
        dummy = Node(-1)
        new_head = dummy
        curr = head
        node_indices = {}
        from_index_to = {}
        deep_pointers = {}
        index = 0
        while curr:
            node = Node(curr.val)
            dummy.next = node
            deep_pointers[index] = node
            node_indices[curr] = index
            curr = curr.next
            dummy = dummy.next
            index += 1
        
        curr = head
        index = 0
        while curr:
            if curr.random:
                from_index_to[index] = node_indices[curr.random]
            index += 1
            curr = curr.next
            
        curr = new_head.next
        index = 0
        while curr:
            if from_index_to.get(index) is not None:
                curr.random = deep_pointers[from_index_to[index]]
            index += 1
            curr = curr.next
        return new_head.next
            