class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num/2
        while left <= right:
            mid = left + (right - left)//2
            if mid == num/mid:
                return True
            elif mid > num/mid:
                right = mid - 1
            else:
                left = mid + 1
        if right*right == num or left*left == num:
            return True
        return False
        