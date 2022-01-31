class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_amount = -2**32-1
        max_amount_idx = 0
        for index, value in enumerate(accounts):
            curr_amount = sum(value)
            max_amount = max(max_amount, curr_amount)
        return max_amount