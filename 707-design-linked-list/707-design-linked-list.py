# For singly Linked List
# class MySinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
        
#     # If the index is invalid, return -1
#     def get(self, index: int) -> int:
#         if index >= self.size or index < 0:
#             return -1
        
#         if self.head is None:
#             return -1
        
#         curr = self.head
#         for i in range(index):
#             curr = curr.next
#         return curr.val
    
#     def addAtHead(self, val: int) -> None:
#         node = Node(val, self.head)
#         self.head = node
#         self.size += 1

#     def addAtTail(self, val: int) -> None:
#         curr = self.head
#         if curr is None:
#             self.addAtHead(val)
#         else:
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = Node(val)
#             self.size += 1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.size:
#             return -1
#         if index == 0:
#             self.addAtHead(val)
#         else:
#             curr = self.head
#             prev = curr
#             for i in range(index):
#                 prev = curr
#                 curr = curr.next
#             prev.next = Node(val, curr)
#             self.size += 1
        
#     # Delete the indexth node in the linked list, if the index is valid.
#     def deleteAtIndex(self, index: int) -> None:
#         if index >= self.size:
#             return -1
#         curr = self.head
#         if index == 0:
#             self.head = self.head.next
#         else:
#             prev = curr
#             for i in range(index):
#                 prev = curr
#                 curr = curr.next
#             if curr.next is None:
#                 prev.next = None
#             else:
#                 prev.next = curr.next
#         self.size -= 1
        
'''
["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
[[],[0,10],[0,20],[1,30],[0]]
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","deleteAtIndex","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[0],[0],[1]]
["MyLinkedList","addAtHead","get","addAtTail","get","addAtIndex","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[0],[3],[1],[1,2],[4,4],[1],[1],[1]]
["MyLinkedList","addAtHead","deleteAtIndex"]
[[],[1],[0]]
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[0],[0]]
'''
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class Node:
    def __init__(self, val = 0, anext = None, prev = None):
        self.val = val
        self.next = anext
        self.prev = prev
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index):
        if self.size and 0 <= index < self.size:
            curr = self.head
            while index > 0:
                curr = curr.next
                index -= 1
            return curr.val
        else:
            return -1
    
    def addAtHead(self, val):
        node = Node(val, self.head, None)
        self.head = node
        self.size += 1
    
    def addAtTail(self, val):
        if not self.size:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        node = Node(val, None, curr)
        curr.next = node
        self.size += 1
            
    def deleteAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        if index < self.size and index > 0:
            curr = self.head
            while index > 0:
                prev = curr
                curr = curr.next
                index -= 1
            anext = None
            if curr is not None:
                anext = curr.next
            prev.next = anext
            self.size -= 1
        
    def addAtIndex(self, index, val):
        if index > self.size or index < 0:
            return self.head
        
        if not self.size or index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        curr = self.head
        while index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        anext = curr
        node = Node(val, anext, prev)
        anext.prev = node
        if prev:
            prev.next = node
        self.size += 1