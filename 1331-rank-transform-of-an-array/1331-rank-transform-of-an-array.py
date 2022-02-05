class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Warm-up Approach 2
        if not arr:
            return arr
        asorted = sorted(arr)
        hashmap = dict()
        rank = 1
        for num in asorted:
            if num in hashmap:
                continue
            hashmap[num] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = hashmap[arr[i]]
        return arr
        
        # Warm-up Approach 1
        # This approach will not work for big data, throws memory owerflow
        if not arr:
            return arr
        amax = max(arr)
        amin = min(arr)
        count = [0]*(amax - amin + 1)
        for val in arr:
            count[val - amin] = 1
        for i in range(1, len(count)):
            count[i] += count[i-1]
        for i in range(len(arr)):
            arr[i] = count[arr[i] - amin]
        return arr