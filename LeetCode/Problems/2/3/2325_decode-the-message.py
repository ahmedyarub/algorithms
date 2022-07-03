class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {}

        i = ord('a')
        for c in key:
            if c != ' ' and c not in dic:
                dic[c] = chr(i)
                i += 1

        return "".join([' ' if c == ' ' else dic[c] for c in message])
