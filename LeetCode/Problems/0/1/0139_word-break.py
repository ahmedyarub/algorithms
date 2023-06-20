class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def traverse(start: int) -> bool:
            nonlocal s, wordDict

            if start == len(s):
                return True

            for word in wordDict:
                if start + len(word) <= len(s) and word == s[start:start + len(word)]:
                    if traverse(start + len(word)):
                        return True

            return False

        return traverse(0)
