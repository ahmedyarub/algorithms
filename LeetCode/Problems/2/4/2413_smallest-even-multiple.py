class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 2 if n % 2 else n


if __name__ == '__main__':
    print(Solution().smallestEvenMultiple(5))  # 10
    print(Solution().smallestEvenMultiple(6))  # 6
