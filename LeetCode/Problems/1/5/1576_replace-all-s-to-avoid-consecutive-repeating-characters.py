class Solution:
    def modifyString(self, s: str) -> str:
        result = []

        for i, c in enumerate(s):
            if c == '?':
                prev = ord(result[i - 1]) if i else ''
                nxt = ord(s[i + 1]) if i < len(s) - 1 else ''
                for nc in range(ord('a'), ord('z')):
                    if nc != prev and nc != nxt:
                        result.append(chr(nc))
                        break
            else:
                result.append(c)

        return "".join(result)
