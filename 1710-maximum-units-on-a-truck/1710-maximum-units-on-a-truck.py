class Solution:
    def countSort(self, A):
        k = 0
        for el in A:
            if k < el[1]:
                k = el[1]
        # create an integer list of size `n` to store the sorted list
        output = [0] * len(A)
    
        # create an integer list of size `k + 1`, initialized by all zero
        freq = [0] * (k + 1)
    
        # using the value of each item in the input list as an index,
        # store each integer's count in `freq[]`
        for el in A:
            freq[el[1]] = freq[el[1]] + 1
    
        # calculate the starting index for each integer
        total = 0
        for i in range(k + 1):
            oldCount = freq[i]
            freq[i] = total
            total += oldCount
    
        # copy to the output list, preserving the order of inputs with equal keys
        for el in A:
            output[freq[el[1]]] = el
            freq[el[1]] = freq[el[1]] + 1
    
        # copy the output list back to the input list
        i = len(A) - 1
        j = 0
        while i >= 0:
            A[j] = output[i]
            j += 1
            i -= 1
        
        return A
    
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = Solution().countSort(boxTypes)
        amax = i = 0
        while i < len(boxTypes) and truckSize > 0:
            box_num = boxTypes[i][0]
            if box_num <= truckSize:
                amax += box_num*boxTypes[i][1]
                truckSize = truckSize - box_num
            else:
                amax += truckSize*boxTypes[i][1]
                return amax
            i += 1
        return amax