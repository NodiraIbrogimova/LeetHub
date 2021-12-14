# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Approach 1
        # Run BFS and check if value is in [low, high]
        # add to to total is so
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if low <= node.val <= high:
                    total += node.val
                if node.val < high:
                    stack.append(node.right)
        return total
        