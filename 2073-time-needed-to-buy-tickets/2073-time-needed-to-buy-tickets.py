class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Approach 1
        # Iterate through the array until tickets[k] becomes 0
        # In each iteration, inc asum with 1sec for each element
        # In case tickets[i] becomes 0 at certain point, return sum directly
        spent = 0
        while tickets[k] > 0:
            i = 0
            while i < len(tickets):
                if tickets[k] == 0:
                    return spent
                if tickets[i] > 0:
                    tickets[i] -= 1
                    spent += 1
                i += 1
        return spent