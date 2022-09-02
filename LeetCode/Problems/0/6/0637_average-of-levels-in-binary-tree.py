class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue, result, s, prev_level, cnt = [(root, 0)], [], 0, 0, 0

        while queue:
            node, level = queue.pop(0)
            if level != prev_level:
                result.append(s / cnt)
                s, cnt = 0, 0
                prev_level = level

            s += node.val
            cnt += 1

            if node.left:
                queue.append((node.left, prev_level + 1))
            if node.right:
                queue.append((node.right, prev_level + 1))

        return result + [s / cnt]
