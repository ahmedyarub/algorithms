class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left

        return sum(expand(s, left, right) // 2 for center in range(len(s)) for left, right in
                   [(center, center), (center, center + 1)])


if __name__ == '__main__':
    print(Solution().countSubstrings("abc"))
