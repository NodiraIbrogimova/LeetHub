class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [0]*(len(encoded)+1)
        arr[0] = first
        i = 0
        while i < len(encoded):
            el = arr[i]
            arr[i+1] = el ^ encoded[i]
            i += 1
        return arr