class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        vi = defaultdict(list)

        for i, v in enumerate(nums):
            vi[v].append(i)

        return sum([(comb[0] * comb[1]) % k == 0 for vis in vi.values() for comb in combinations(vis, 2)])
