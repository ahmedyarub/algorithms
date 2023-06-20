class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not len(digits):
            return []

        return [digit + comb for comb in (self.letterCombinations(digits[1:]) or ['']) for digit in mp[digits[0]][:]]
