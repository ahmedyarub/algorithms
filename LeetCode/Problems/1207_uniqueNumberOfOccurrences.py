class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for a in arr:
            count[a] = count.get(a, 0) + 1

        occ = {}
        for v in count.values():
            if v in occ:
                return False
            else:
                occ[v] = 1

        return True
