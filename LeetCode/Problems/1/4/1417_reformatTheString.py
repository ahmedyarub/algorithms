class Solution:
    def reformat(self, s: str) -> str:
        a = [c for c in s if c.isalpha()]
        b = [c for c in s if c.isdigit()]

        if abs(len(a) - len(b)) > 1:
            return ""

        if len(a) < len(b):
            a, b = b, a

        result = []
        while a:
            result.append(a.pop())
            if b:
                result.append(b.pop())

        return "".join(result)
