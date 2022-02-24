class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        A, currPower, asum = ord('A'), 0, 0
        for i in range(len(columnTitle)-1, -1, -1):
            order = ord(columnTitle[i]) - A + 1
            asum += order*(26**currPower)
            currPower += 1
        return asum

        