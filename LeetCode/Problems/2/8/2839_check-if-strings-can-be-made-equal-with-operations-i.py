class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return ({s1[0], s1[2]} == {s2[0], s2[2]} and
                {s1[1], s1[3]} == {s2[1], s2[3]})
