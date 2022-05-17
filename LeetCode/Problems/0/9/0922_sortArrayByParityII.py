class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        return [item for sublist in zip([e for e in nums if not e % 2], [o for o in nums if o % 2]) for item in sublist]
