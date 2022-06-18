class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        mem = {}
        miss, cnt = 0, 1

        def comb(candidates: List[int], target: int):
            nonlocal mem, miss, cnt

            result = set()
            cnt += 1
            if target not in mem:
                miss += 1
                for c in candidates:
                    if c == target:
                        result.add((c,))
                    elif c < target:
                        for nx in comb(candidates, target - c):
                            result.add(tuple(sorted(([c] + list(nx)))))
                    else:
                        break
                mem[target] = result
            return mem[target]

        return list(map(list, comb(sorted(candidates), target)))
