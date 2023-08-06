class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        result, cnt0, cnt1 = 0, 0, 0

        for c in s:
            if c == '1':
                cnt1 += 1
                result = max(result, min(cnt0, cnt1) * 2)
            else:
                if cnt1:
                    cnt0, cnt1 = 1, 0
                else:
                    cnt0 += 1

        return result
