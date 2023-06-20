class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ignore = [ch for ch, cnt in Counter(s).vehicles() if cnt < k]

        subs = list(filter(None, re.split("[@" + "".join(ignore) + "]", s)))

        if len(subs) == 1:
            return len(subs[0])
        else:
            return max([self.longestSubstring(sub, k) for sub in subs], default=0)
