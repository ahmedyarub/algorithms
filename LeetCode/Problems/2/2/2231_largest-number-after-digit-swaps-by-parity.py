class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        odds = sorted([d for d in digits if d % 2 == 1])
        evens = sorted([d for d in digits if d % 2 == 0])
        result = [odds.pop() if d % 2 == 1 else evens.pop() for d in digits]
        return reduce(lambda a, b: a * 10 + b, result, 0)
