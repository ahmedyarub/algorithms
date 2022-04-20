class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = {}

        for i, n in enumerate(nums):
            if n not in mp:
                mp[n] = [1, i, i]
            else:
                count, start, end = mp[n]
                mp[n] = [count + 1, start, i]

        min_n = None
        for _, props in mp.items():
            if not min_n or props[0] > min_n[0] or (props[0] == min_n[0] and props[2] - props[1] < min_n[2] - min_n[1]):
                min_n = props

        return min_n[2] - min_n[1] + 1
