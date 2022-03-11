class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(remaining, path):
            if not remaining:
                result.append(path.copy())
                return
            
            for i, el in enumerate(remaining):
                path.append(el)
                dfs(remaining[:i]+remaining[i+1:], path)
                path.pop()
        
        dfs(nums, [])
        return result