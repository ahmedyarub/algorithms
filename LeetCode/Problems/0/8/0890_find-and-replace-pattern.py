class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []

        for word in words:
            mp, similar, pseen = {}, True, set()

            for cw, cp in zip(word, pattern):
                if cw not in mp:
                    if cp in pseen:
                        similar = False
                        break
                    mp[cw] = cp
                else:
                    if mp[cw] != cp:
                        similar = False
                        break

                pseen.add(cp)

            if similar:
                result.append(word)

        return result
