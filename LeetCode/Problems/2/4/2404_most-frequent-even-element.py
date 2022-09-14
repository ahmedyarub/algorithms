class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mc = Counter(num for num in nums if not num % 2).most_common()
        return min([n for n, cnt in mc if cnt == mc[0][1]], default=-1)
