class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for st in strs:
            map[tuple(sorted(st))].append(st)

        return list(map.values())
