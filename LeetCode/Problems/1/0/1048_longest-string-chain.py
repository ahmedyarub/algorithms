class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lmp, mem = defaultdict(list), dict()
        for word in words:
            lmp[len(word)].append(word)

        def cmp(word1, word2):
            wi1, wi2 = 0, 0

            while wi1 < len(word1):
                if word1[wi1] != word2[wi2]:
                    if wi1 != wi2:
                        return False
                    else:
                        wi2 += 1
                else:
                    wi1 += 1
                    wi2 += 1

            return True

        def traverse(cnt: int, curw: str):
            nonlocal lmp, mem

            if curw in mem:
                return mem[curw]

            result = max([traverse(cnt + 1, nword) for nword in lmp[len(curw) + 1] if cmp(curw, nword)], default=0) + 1
            mem[curw] = result
            return result

        return max([traverse(1, word) for word in words])
