class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num in arr1:
            low, high = 0, len(arr2)-1
            while high - low > 1:
                mid = (high + low)//2
                if arr2[mid] <= num:
                    low = mid
                else:
                    high = mid
            # check count
            closest_distance = min(abs(num - arr2[low]), abs(num-arr2[high]))
            if closest_distance > d:
                count += 1
        return count