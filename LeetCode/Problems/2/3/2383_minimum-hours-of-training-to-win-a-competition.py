class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        en, ex, an, ax = 0, 0, 0, 0

        for ener, exp in zip(energy, experience):
            if ener >= en:
                an += (ener - en + 1)
                en += (ener - en + 1)
            if exp >= ex:
                ax += (exp - ex + 1)
                ex += (exp - ex + 1)

            en -= ener
            ex += exp

        return max(0, (an - initialEnergy)) + max(0, (ax - initialExperience))
