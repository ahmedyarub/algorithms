class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, cur_line = 0, 0

        for c in s:
            c_width = widths[ord(c) - ord('a')]
            if c_width + cur_line > 100:
                lines += 1
                cur_line = c_width
            else:
                cur_line += c_width

        return [lines + 1, cur_line]
