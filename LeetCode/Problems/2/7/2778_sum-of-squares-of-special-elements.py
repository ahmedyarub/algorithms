class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total, n = 0, len(nums)

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]
                j = n // i

                if j != i:
                    total += nums[j - 1] * nums[j - 1]

        return total


if __name__ == '__main__':
    print(Solution().sumOfSquares([1, 2, 3, 4]))
