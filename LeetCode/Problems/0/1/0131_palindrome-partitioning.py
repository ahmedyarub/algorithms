class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @lru_cache(maxsize=None)
        def isPalindrome(st: int, end: int) -> bool:
            return s[st:end] == s[st:end][::-1]

        result = []

        def traverse(start: int, path: List[str]):
            nonlocal result, s
            if start < len(s):
                for to in range(start + 1, len(s) + 1):
                    if isPalindrome(start, to):
                        path.append(s[start:to])
                        traverse(to, path)
                        path.pop()
            else:
                result.append(path[:])

        traverse(0, [])

        return result
