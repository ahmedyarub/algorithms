class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = [i for i, sc in enumerate(s) if sc == c]

        cur_pos = 0
        result = []
        for i, sc in enumerate(s):
            if cur_pos < len(pos) - 1 and abs(pos[cur_pos + 1] - i) < abs(pos[cur_pos] - i):
                cur_pos += 1

            result.append(abs(pos[cur_pos] - i))

        return result
