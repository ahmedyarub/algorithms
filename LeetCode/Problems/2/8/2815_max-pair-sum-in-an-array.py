class Solution:
    def maxSum(self, nums: List[int]) -> int:
        result, mp = -1, {}

        for num in nums:
            digit = max([int(c) for c in str(num)])
            if digit in mp:
                result = max(result, num + mp[digit])
                mp[digit] = max(mp[digit], num)
            else:
                mp[digit] = num

        return result
