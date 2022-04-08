class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = [Counter(s) for s in words]

        result = []
        for ch in counts[0].keys():
            result += [ch] * min([count[ch] if ch in count else 0 for count in counts])

        return result
