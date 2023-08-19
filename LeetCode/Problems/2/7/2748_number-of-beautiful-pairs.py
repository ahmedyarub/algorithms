class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0

        frst = list(map(lambda x: int(str(x)[0]), nums))
        last = list(map(lambda x: x % 10, nums))

        for i, n1 in enumerate(frst):
            for n2 in last[i + 1:]:
                ans += (gcd(n1, n2) == 1)

        return ans
