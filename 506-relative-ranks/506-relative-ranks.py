class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indicies, result = {value:idx for idx, value in enumerate(score)}, [0 for _ in score]
        ranks = {0:"Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        for idx, value in enumerate(sorted(score)[::-1]):
            index = indicies[value]
            result[index] = ranks[idx] if idx in range(3) else str(idx+1)
        return result
        
#         amax = max(scores)
#         count = [0]*(amax+1)
#         for score in scores:
#             count[score] = 1
            
#         # for i in range(1, len(count)):
#         #     count[i] += count[i-1]
            
#         print('count: ', count)
        
#         i = len(count)-1
#         position = 0
#         places  = ["Gold Medal","Silver Medal","Bronze Medal"]
        
#         while position < 3 and i >= 0:
#             # while position < 3 and i >= 0:
#             if count[i] == 1:
#                 count[i] = places[position]
#                 position += 1
#                 # i -= 1
#             i -= 1
#         position += 1
#         while i >= 0:
#             if count[i] == 0:
#                 count[i] = str(position)
#                 position += 1
#             i -= 1
#         print('count is: ', count, i)
#         i = 0
#         while i < len(scores):
#             scores[i] = count[scores[i]]
#             i += 1
#         return scores

        
        
        '''
        Approach 1:
        1. Sort the score to know the expected position of the score[i] and save in sorted_score
        2. Hashmap for storing original position of score[i] in score
        3. Once iteration over named awards is over, start with order which is fourth place in competition
            Find original index of sorted_score[i] in hashmap
            In that index of score, store awards[i] -> order
            
        Time complexity:
        Sort = O(n*logn)
        Awards = O(3)
        Hashmap = O(n) as numbers are unique
        Update score = O(n)
        
        Overall =  O(n*logn) + O(3) +  O(n) + O(n) =  O(n*logn) + O(2n) + O(1) =  O(n*logn)
        
        Space complexity:
        Sorted score = O(n)
        Hashmap = O(n)
        Awards = O(3)
        
        Overall = O(n)
        '''
        
        score_sorted = sorted(score, reverse=True)
        awards = ["Gold Medal","Silver Medal", "Bronze Medal"]
        hashmap = dict()
        i = 0
        while i < len(score):
            hashmap[score[i]] = i
            i += 1
        
        i = 0
        while i < len(awards) and i < len(score):
            score[hashmap[score_sorted[i]]] = awards[i]
            i += 1
        order = 4
        while i < len(score_sorted):
            score[hashmap[score_sorted[i]]] = str(order)
            order += 1
            i += 1
        return score
        
        
        
        
        
        
        
        