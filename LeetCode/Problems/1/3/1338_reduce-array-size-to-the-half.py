class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        result, removed = 0, 0

        for cnt in sorted([cnt for _, cnt in Counter(arr).items()], reverse=True):
            removed += cnt
            result += 1
            if len(arr) // 2 <= removed:
                return result
