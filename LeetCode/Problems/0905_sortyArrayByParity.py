class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        head = 0
        tail = len(nums) - 1

        while head < tail:
            if nums[head] % 2:
                if not nums[tail] % 2:
                    nums[head], nums[tail] = nums[tail], nums[head]
                tail -= 1
            else:
                head += 1

        return nums
