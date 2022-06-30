class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lens = [len(wd) for wd in wordDict]
        mn = min(lens)

        @lru_cache(maxsize=None)
        def check(start: int, end: int) -> bool:
            nonlocal s, wordDict, mn
            return start == end or s[start:end] in wordDict or any(
                [check(start, e) and check(e, end) for e in range(start + mn, end)])

        return check(0, len(s))
