class Solution:
    def reformatNumber(self, number: str) -> str:
        digits, result, cur = [n for n in number if n.isnumeric()], [], 0

        while cur < len(digits) - 1:
            rem = len(digits) - cur

            if rem > 4:
                d = 3
            elif rem == 4:
                d = 2
            else:
                d = rem

            result.append("".join(digits[cur:cur + d]))
            cur += d

        return "-".join(result)
