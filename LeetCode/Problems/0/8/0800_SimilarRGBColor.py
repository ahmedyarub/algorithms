class Solution:
    def similarRGB(self, color: str) -> str:
        return '#' + ''.join([hex(round(c / int('0x11', 16)))[2] * 2 for c in
                              [int(color[i:i + 2], 16) for i in range(1, len(color), 2)]])
