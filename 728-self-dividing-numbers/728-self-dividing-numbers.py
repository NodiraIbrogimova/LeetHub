class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for number in range(left, right+1):
            value = str(number)
            for digit in value:
                if int(digit) == 0 or number % int(digit) != 0:
                    break
            else:
                result.append(number)
        return result
        