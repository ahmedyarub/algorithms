class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        known = set()

        def traverse() -> List[List[int]]:
            results = []
            for num in nums:
                if num not in known:
                    known.add(num)
                    subgroups = traverse()
                    results.extend([subgroup + [num] for subgroup in subgroups] if subgroups else [[num]])
                    known.remove(num)

            return results

        return traverse()
