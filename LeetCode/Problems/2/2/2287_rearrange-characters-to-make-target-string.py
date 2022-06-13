class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc = Counter(list(s))
        return min([sc[ch] // cn for ch, cn in Counter(list(target)).items()])
