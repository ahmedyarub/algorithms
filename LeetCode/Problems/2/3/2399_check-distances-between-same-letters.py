class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        mp = defaultdict(list)
        for i, c in enumerate(s):
            mp[c].append(i)

        for c, d in enumerate(distance):
            ch = chr(ord('a') + c)
            if ch in mp:
                if mp[ch][1] - mp[ch][0] != d + 1:
                    return False

        return True