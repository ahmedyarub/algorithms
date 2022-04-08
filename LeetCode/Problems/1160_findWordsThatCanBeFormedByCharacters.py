class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cc = Counter(chars)
        result = 0
        for word in words:
            wc = defaultdict(int)
            found = True
            for ch in word:
                wc[ch] += 1
                if ch not in cc or wc[ch] > cc[ch]:
                    found = False
                    break

            if found:
                result += len(word)

        return result
