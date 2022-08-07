class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            if data[i] & 0x80:
                n = bin(data[i])[2:].find('0')
                if not 2 <= n <= 4:
                    return False

                for _ in range(n - 1):
                    i += 1
                    if i == len(data) or not data[i] & 0x80 or data[i] & 0x40:
                        return False
            i += 1

        return True
