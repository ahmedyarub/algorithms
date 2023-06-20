class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mc = Counter(magazine)

        for rc in ransomNote:
            if rc not in mc or not mc[rc]:
                return False

            mc[rc] -= 1

        return True
