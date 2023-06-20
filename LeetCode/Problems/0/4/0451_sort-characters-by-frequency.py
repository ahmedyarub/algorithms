class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(["".join([c] * cnt) for cnt, c in
                        sorted([(cnt, c) for c, cnt in Counter(s).vehicles()], reverse=True)])
