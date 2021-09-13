class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        i = 0
        while i < len(num_str):
            if num_str[i] == '6':
                return int(num_str[:i] +'9'+ num_str[i+1:])
            i += 1
        return num
        