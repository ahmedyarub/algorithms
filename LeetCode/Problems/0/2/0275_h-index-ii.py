class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= len(citations) - mid:
                r = mid - 1
            else:
                l = mid + 1

        return len(citations) - l
