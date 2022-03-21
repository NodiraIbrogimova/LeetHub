# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Step 1
        children  = set()
        for parent, child, isLeft in descriptions:
            if child not in children:children.add(child)
    
        hashmap = dict()
        for key in descriptions:
            hashmap[key[0]] = [None, None]
            if key[1] not in children:
                children.add(key[1])
            
        for parent, child, isLeft in descriptions:
            if isLeft:
                hashmap[parent] = [child, hashmap.get(parent)[1]]
            else:
                hashmap[parent] = [hashmap.get(parent)[0], child]
                
        # Step 2 - Finding root
        root = None
        for parent, child, isLeft in descriptions:
            if parent not in children:
                root = parent
                break
            elif child not in children:
                root = child
                break
        # Step 3
        def dfs(node):
            if not node:
                return node
            
            if hashmap.get(node) == None:
                return TreeNode(node)
            
            return TreeNode(node,dfs(hashmap[node][0]), dfs(hashmap[node][1]))
            
        return dfs(root)
        
        
        