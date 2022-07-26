class Solution:
    def generateAbbreviations(self, word):
        result = []

        def helper(pos: int, cur: str, count: int):
            if len(word) == pos:
                result.append(cur + str(count) if count > 0 else cur)
            else:
                helper(pos + 1, cur, count + 1)
                helper(pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0)

        helper(0, '', 0)
        return result
