class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        mp, result, start, cur = defaultdict(int), 0, 0, 0

        for c in s:
            mp[c] += 1
            cur += 1
            while len(mp.keys()) > 2:
                sc = s[start]
                if mp[sc] == 1:
                    del mp[sc]
                else:
                    mp[sc] -= 1

                start += 1
                cur -= 1
            result = max(result, cur)

        return result
