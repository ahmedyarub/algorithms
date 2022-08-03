class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = 1

        for power in b:
            result = ((pow(result, 10) % 1337) * (pow(a, power) % 1337)) % 1337

        return result

    print(Solution().superPow(1, [4, 3, 3, 8, 5, 2]))
