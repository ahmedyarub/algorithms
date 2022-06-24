class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result, ranges = [], [(1, 0, 9), (2, 10, 99), (3, 100, 255)]

        def traverse(prev: List[str], i: int):
            nonlocal result, ranges
            if len(prev) == 4:
                if i == len(s):
                    result.append(".".join(prev))
            else:
                minrem, maxrem = (4 - len(prev) - 1), (4 - len(prev) - 1) * 3

                for ln, frm, to in ranges:
                    if minrem <= len(s) - i - ln <= maxrem and frm <= int(s[i:i + ln]) <= to:
                        traverse(prev + [s[i:i + ln]], i + ln)

        traverse([], 0)
        return result
