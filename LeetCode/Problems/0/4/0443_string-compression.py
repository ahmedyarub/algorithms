class Solution:
    def compress(self, chars: List[str]) -> int:
        iw, ir = 0, 0

        while ir < len(chars):
            chars[iw] = chars[ir]
            count = 1

            while ir < len(chars) - 1 and chars[ir] == chars[ir + 1]:
                ir += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[iw + 1] = c
                    iw += 1

            ir += 1
            iw += 1

        return iw
