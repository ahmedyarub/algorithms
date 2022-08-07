class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        digits, result = ceil(log10(n) + 0.1), []

        def gen(prev: int, start: int):
            for i in range(start, min(n + 1, 10)):
                cur = prev + i
                if cur > n:
                    return
                result.append(cur)
                gen(cur * 10, 0)

        gen(0, 1)

        return result
