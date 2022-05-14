class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for n in range(left, right + 1):
            for d in set([int(c) for c in str(n)]):
                if not d or n % d:
                    break
            else:
                result.append(n)

        return result
