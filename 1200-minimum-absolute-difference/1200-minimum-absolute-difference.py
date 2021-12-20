class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr.sort()
        amin = 2**32-1
        
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            
            if diff < amin:
                amin = diff
                result = []
                result.append([arr[i], arr[i+1]])
            elif diff == amin:
                result.append([arr[i], arr[i+1]])
        return result
                
        