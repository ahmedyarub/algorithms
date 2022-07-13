class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []

        cnt1, cnt2, n1, n2 = 0, 0, None, None
        for num in nums:
            if n1 == num:
                cnt1 += 1
            elif n2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                n1 = num
                cnt1 += 1
            elif cnt2 == 0:
                n2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        result = []
        for c in [n1, n2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)

        return result
