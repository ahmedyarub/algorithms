class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        head = 0
        tail = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(head) > abs(tail):
                result[i](head ** 2)
                head += 1
            else:
                result[i] = (tail ** 2)
                tail -= 1

        return result
