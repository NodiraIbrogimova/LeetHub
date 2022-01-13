class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0
        head, tail = 0, len(heights)-1
        while head < tail:
            height = min(heights[head], heights[tail])
            width = (tail-head)
            max_height = max(max_height, width*height)
            if heights[head] < heights[tail]:
                head += 1
            else:
                tail -= 1
        return max_height
        