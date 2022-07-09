class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        score, dq = nums[0], [(0, nums[0])]

        for i in range(1, len(nums)):
            while dq and dq[0][0] < i - k:
                dq.pop(0)

            score = dq[0][1] + nums[i]

            while dq and score >= dq[-1][1]:
                dq.pop()

            dq.append((i, score))

        return score
