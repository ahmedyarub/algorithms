class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        @cache
        def traverse(remaining: int, start: int) -> List[List[int]]:
            nonlocal candidates
            cur_results = []

            i = start
            while i < len(candidates):
                candidate = candidates[i]

                if candidate == remaining:
                    cur_results.append([candidate])
                elif candidate < remaining:
                    cur_results.extend(
                        [[candidate] + next_subgroup for next_subgroup in traverse(remaining - candidate, i)]
                    )
                else:
                    break

                i += 1
                while i < len(candidates) and candidates[i] == candidate:
                    i += 1

            return cur_results

        return traverse(target, 0)
