class Solution:
    def wordPatternMatch(self, pattern, str):
        mp = {}

        def dfs(pi: int, sstart: int):
            nonlocal mp
            if len(pattern) == pi:
                return len(str) == sstart

            for send in range(sstart + 1, len(str) - (len(pattern) - pi) + 2):
                if pattern[pi] not in mp and str[sstart:send] not in mp.values():
                    mp[pattern[pi]] = str[sstart:send]
                    if dfs(pi + 1, send):
                        return True
                    del mp[pattern[pi]]
                elif pattern[pi] in mp:
                    if mp[pattern[pi]] == str[sstart:send]:
                        if dfs(pi + 1, send):
                            return True
                    elif len(mp[pattern[pi]]) <= send - sstart:
                        return False

            return False

        return dfs(0, 0)
