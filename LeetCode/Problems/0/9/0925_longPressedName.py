class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ni = ti = 0
        prev = None
        while ni < len(name) and ti < len(typed):
            if typed[ti] != name[ni]:
                if typed[ti] != prev:
                    return False
                else:
                    ti += 1
            else:
                prev = name[ni]
                ni += 1
                ti += 1

        while ti < len(typed) and typed[ti] == prev:
            ti += 1

        return ni == len(name) and ti == len(typed)
