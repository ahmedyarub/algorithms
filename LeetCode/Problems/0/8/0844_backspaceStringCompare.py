class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def trans(st):
            result = []
            for c in st:
                if c != '#':
                    result.append(c)
                elif result:
                    result.pop()

            return result

        return trans(s) == trans(t)
