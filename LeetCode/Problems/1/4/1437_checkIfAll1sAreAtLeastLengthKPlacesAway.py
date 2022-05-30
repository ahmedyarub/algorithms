class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = float('inf')

        for num in nums:
            if num:
                if counter < k:
                    return False

                counter = 0
            else:
                counter += 1

        return True
