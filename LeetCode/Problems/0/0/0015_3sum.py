class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, result = 0, []

        def twoSum(i):
            nonlocal result
            seen = set()

            j = i + 1
            while j < len(nums):
                compl = -nums[i] - nums[j]

                if compl in seen:
                    result.append([nums[i], nums[j], compl])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1

                seen.add(nums[j])
                j += 1

        while i < len(nums) and nums[i] <= 0:
            twoSum(i)

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            i += 1

        return result
