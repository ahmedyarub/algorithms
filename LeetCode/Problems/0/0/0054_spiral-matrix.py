class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result, cur_dir, dir_offset, side_limit, size, cnt, c, r = \
            [], 0, [[0, 1], [1, 0], [0, -1], [-1, 0]], [len(matrix[0]) - 1, len(matrix) - 1, 0, 1], len(matrix) * len(
                matrix[0]), 0, 0, 0

        while cnt < size:
            result.append(matrix[r][c])
            cnt += 1

            if (cur_dir % 2 and r == side_limit[cur_dir]) or (not cur_dir % 2 and c == side_limit[cur_dir]):
                if cur_dir <= 1:
                    side_limit[cur_dir] -= 1
                else:
                    side_limit[cur_dir] += 1

                cur_dir = (cur_dir + 1) % 4

            c, r = c + dir_offset[cur_dir][1], r + dir_offset[cur_dir][0]

        return result
