class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for col in range(len(strs[0])):
            prev = 0
            for row in range(len(strs)):
                c = ord(strs[row][col])
                if c < prev:
                    result += 1
                    break

                prev = c

        return result
