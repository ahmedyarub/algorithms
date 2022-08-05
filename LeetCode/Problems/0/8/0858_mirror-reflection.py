class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        d = lcm(p, q)

        if not (d // q) % 2:
            return 2

        return (d // p) % 2
