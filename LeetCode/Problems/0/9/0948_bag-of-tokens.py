class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right, result = 0, len(tokens) - 1, 0

        while right - left > 1 or (left < len(tokens) and power >= tokens[left]):
            if power < tokens[left]:
                if not result:
                    return 0
                power += tokens[right]
                right -= 1
                result -= 1
            else:
                power -= tokens[left]
                left += 1
                result += 1

        return result
