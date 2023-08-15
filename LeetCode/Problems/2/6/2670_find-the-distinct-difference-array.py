class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = defaultdict(int)
        suffix = Counter(nums)
        result = []
        for x in nums:
            prefix[x] += 1
            suffix[x] -= 1
            if suffix[x] == 0:
                del suffix[x]
            result.append(len(prefix) - len(suffix))
        return result
