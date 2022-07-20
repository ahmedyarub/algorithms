class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        @cache
        def find(w: str) -> bool:
            wi, si = 0, 0

            while si < len(s) and wi < len(w):
                if w[wi] == s[si]:
                    wi += 1

                si += 1

            return wi == len(w)

        return sum([find(word) for word in words])
