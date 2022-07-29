class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        mp, i, result = defaultdict(int), 0, 0

        for j, c in enumerate(s):
            mp[c] += 1

            while len(mp.keys()) > k:
                cur = s[i]
                mp[cur] -= 1

                if not mp[cur]:
                    del mp[cur]

                i += 1

            result = max(result, j - i + 1)

        return result
