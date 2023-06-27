class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt, start = 0, 0
        while cnt < len(nums):
            tmp = nums[start]
            i = start
            while True:
                nxt_i = (i + k) % len(nums)
                nums[nxt_i], tmp = tmp, nums[nxt_i]
                cnt += 1
                i = (i + k) % len(nums)

                if cnt == len(nums):
                    return
                elif i == start:
                    start += 1
                    break
