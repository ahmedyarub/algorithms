from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = dict()
        for i in range(len(nums)):
            n = nums[i]

            if target - n in val_index:
                return [i, val_index[target - n]]
            else:
                val_index[n] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
