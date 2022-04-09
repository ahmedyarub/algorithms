class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_pos = dict()

        for i, c in enumerate(nums):
            if c in last_pos and i - last_pos[c] <= k:
                return True

            last_pos[c] = i

        return False
