class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result, levels = [], set()

        def traverse(node: Optional[TreeNode], level: int):
            if not node:
                return

            if level not in levels:
                result.append(node.val)
                levels.add(level)

            traverse(node.right, level + 1)
            traverse(node.left, level + 1)

        traverse(root, 0)

        return result
