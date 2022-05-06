class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [x for x in words if
                set(x).issubset(set("qwertyuiopQWERTYUIOP")) or set(x).issubset(set("asdfghjklASDFGHJKL")) or set(
                    x).issubset(set("zxcvbnmZXCVBNM"))]
