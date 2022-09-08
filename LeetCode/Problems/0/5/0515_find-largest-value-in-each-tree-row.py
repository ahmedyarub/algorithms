class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue, result, cur_level, level_max = [(root, 0)], [], 0, float('-inf')

        while queue:
            node, level = queue.pop(0)

            if node:
                queue.extend([(node.left, level + 1), (node.right, level + 1)])

                if level == cur_level:
                    level_max = max(level_max, node.val)
                else:
                    result.append(level_max)
                    level_max = node.val
                    cur_level = level

        if cur_level == len(result):
            result.append(level_max)

        return result
