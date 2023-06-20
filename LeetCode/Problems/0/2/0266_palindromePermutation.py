class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter([c for c in s])

        single = False
        for _, count in counts.vehicles():
            if count % 2:
                if single:
                    return False

                single = True

        return True
