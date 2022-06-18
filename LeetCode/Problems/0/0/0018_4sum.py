class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result, left, right = [], 0, len(nums) - 1

            while left < right:
                l = nums[left]
                r = nums[right]
                s = l + r

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    while nums[left] == l and left < right:
                        left += 1

                    while nums[right] == r and left < right:
                        right -= 1

            return result

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if k == 2:
                return twoSum(nums, target)
            result = []
            for i in range(len(nums) - k + 1):
                if nums[i] * k > target or nums[-1] * k < target:
                    break
                result.extend([[nums[i]] + res for res in kSum(nums[i + 1:], target - nums[i], k - 1)])

            return result

        nums.sort()
        return list(map(list, set(map(tuple, kSum(nums, target, 4)))))
