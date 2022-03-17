class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Approach 2: From Discussions
        
        # The elements on left of k come first, so the time spent on them are always calculated
        # as they are first in the queue
        
        # The elements coming akter kth elements might not be waited for 
        # them to complete getting orders as by that time kth buyer might 
        # have finished buying all tickets
        # That's why count them as one second less than the kth number or itself if < tickets[k]
        
        time_spent = 0
        for i in range(k+1):
            time_spent += min(tickets[k], tickets[i])
        for i in range(k+1, len(tickets)):
            time_spent += min(tickets[k]-1, tickets[i])
        return time_spent
    
        # Approach 1
        # Iterate through the array until tickets[k] becomes 0
        # In each iteration, inc asum with 1sec for each element
        # In case tickets[i] becomes 0 at certain point, return sum directly
        time_spent = 0
        while tickets[k] > 0:
            i = 0
            while i < len(tickets):
                if tickets[k] == 0:
                    return time_spent
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time_spent += 1
                i += 1
        return time_spent