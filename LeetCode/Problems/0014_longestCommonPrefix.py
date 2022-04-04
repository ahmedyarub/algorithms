class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            si = 0

            while len(strs[i]) > si < len(prefix) and prefix[si] == strs[i][si]:
                si += 1

            prefix = prefix[:si]

        return prefix
