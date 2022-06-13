class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join([str(sum(list(map(int, list(s[i:i + k]))))) for i in range(0, len(s), k)])

        return s
