class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp, result, ln = defaultdict(int), 0, 0

        for i, c in enumerate(s):
            mp[c] += 1
            ln += 1

            while ln - max(mp.values()) > k:
                mp[s[i - ln + 1]] -= 1
                ln -= 1

            result = max(result, ln)

        return result
