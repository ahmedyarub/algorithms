class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ch = [c.upper() for c in s if c != '-']
        result = [''.join(ch[0:len(ch) % k])]

        p = ''
        for i in range(len(result[0]), len(ch), k):
            result.append("".join(ch[i:i + k]))

        return '-'.join(filter(None, result))
