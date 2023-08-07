class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        result = 0

        @cache
        def is_prime(n: int) -> bool:
            if n == 2:
                return True

            if not n % 2 or n == 1:
                return False

            for dv in range(3, floor(sqrt(n)) + 1, 2):
                if not n % dv:
                    return False

            return True

        for i in range(len(nums)):
            result = max(result,
                         nums[i][i] if is_prime(nums[i][i]) else 0,
                         nums[i][len(nums) - i - 1] if is_prime(nums[i][len(nums) - i - 1]) else 0)

        return result
