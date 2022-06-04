class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result, cur, i = 0, 0, 0

        while i <= len(sequence) - len(word):
            if sequence[i:i + len(word)] == word:
                cur += 1
                result = max(result, cur)
                i += len(word)
            else:
                if cur>0:
                    i-=(len(word)-1)
                else:
                    i += 1
                cur = 0

        return result


if __name__ == '__main__':
    print(Solution().maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
