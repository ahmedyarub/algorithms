class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isAdditiveNumber(prev1: str, prev2: str, start: int) -> bool:
            nxt = str(int(prev1) + int(prev2))
            if nxt == num[start:start + len(nxt)]:
                if start + len(nxt) == len(num):
                    return True
                else:
                    return isAdditiveNumber(prev2, nxt, start + len(nxt))
            else:
                return False

        return any([isAdditiveNumber(num[:end1], num[end1:end2], end2) for end1 in range(1, len(num) - 1) for end2 in
                    range(end1 + 1, len(num))
                    if len(num[:end1]) == len(str(int(num[:end1])))
                    and len(num[end1:end2]) == len(str(int(num[end1:end2])))])
