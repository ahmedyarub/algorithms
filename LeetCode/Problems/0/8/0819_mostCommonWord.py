class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = Counter(re.split('\W+', paragraph.lower()))
        for b in banned:
            if b in counts:
                del counts[b]

        return max(counts, key=counts.get)
