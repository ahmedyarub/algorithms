class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = defaultdict(int)

        for i in range(len(s) - 9):
            mp[s[i:i + 10]] += 1

        return [rs for rs, cnt in mp.items() if cnt > 1]
