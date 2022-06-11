class Solution:
    def isDecomposable(self, s: str) -> bool:
        two, cnt, prev = False, 0, None

        for ch in s:
            if ch != prev:
                if cnt % 3 == 2:
                    if two:
                        return False
                    else:
                        two = True
                elif cnt % 3:
                    return False

                cnt = 0

            prev = ch
            cnt += 1

        return (two and not cnt % 3) or cnt % 3 == 2
