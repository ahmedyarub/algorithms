class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right, s = 0, len(numbers), float('inf')

        while s != target:
            while s > target:
                right -= 1
                s = numbers[left] + numbers[right]

            while s < target:
                left += 1
                s = numbers[left] + numbers[right]

        return [left + 1, right + 1]
