class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return gcd(*Counter(deck).values()) >= 2
