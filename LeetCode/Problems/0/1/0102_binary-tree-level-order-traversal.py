class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, level_result, cur_level, queue = [], [], 0, ([[0, root]] if root else [])

        while queue:
            level, node = queue.pop(0)

            if level != cur_level:
                result.append(level_result)
                level_result = []
                cur_level = level

            level_result.append(node.val)
            if node.left:
                queue.append([cur_level + 1, node.left])
            if node.right:
                queue.append([cur_level + 1, node.right])

        return result + ([level_result] if level_result else [])
