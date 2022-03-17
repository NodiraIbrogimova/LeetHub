class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        '''
        TC: O(3*101) = O(1)
        SC: O(3*101) = O(1)
        '''
        MAX_VALUE = 101
        count = [ [0]*(MAX_VALUE+1) for i in range(3)]
        order = 0
        for val in nums1:
            count[order][val] = 1
        order += 1
        for val in nums2:
            count[order][val] = 1
        order += 1
        for val in nums3:
            count[order][val] = 1
        for i in range(MAX_VALUE+1):
            count[0][i] += (count[1][i] + count[2][i])
        result = []
        for i in range(MAX_VALUE+1):
            if count[0][i] > 1:
                result.append(i)
        return result
            