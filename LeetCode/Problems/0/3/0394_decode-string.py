class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def decodeString() -> List[str]:
            nonlocal s, i
            result = []

            if i == len(s):
                return result

            while i < len(s) and s[i] != ']':
                while i < len(s) and s[i].isalpha():
                    result.append(s[i])
                    i += 1

                if i >= len(s) or s[i] == ']':
                    i += 1
                    return result

                start = i
                while s[i].isdigit():
                    i += 1

                rep = 1 if i == start else int(s[start:i])

                i += 1
                result.extend(decodeString() * rep)

            i += 1

            return result

        return "".join(decodeString())
