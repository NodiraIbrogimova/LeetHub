class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return digits
        
        result = []
        num_letter = {"2":["a", "b", "c"], '3':['d', 'e','f'], '4':['g', 'h', 'i'], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        
        def permute(digits, path, i):
            if i >= len(digits):
                result.append("".join(path.copy()))
                return

            digits_path = num_letter[digits[i]]
            for j, achar in enumerate(digits_path):
                path.append(achar)
                permute(digits, path, i+1)
                path.pop()
        
        
        permute(digits, [], 0)
        return result