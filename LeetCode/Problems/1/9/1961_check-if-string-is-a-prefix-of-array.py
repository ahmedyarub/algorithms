class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s2 = ""

        for word in words:
            s2 = s2 + word

            if len(s2) > len(s):
                return False
            elif len(s2) == len(s):
                break

        return s == s2
