class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        return reduce(lambda result, pair: [result[0] + pair[0], result[1] + pair[1]],
                      [[cnt // 2, cnt % 2] for cnt in Counter(nums).values()], [0, 0])
