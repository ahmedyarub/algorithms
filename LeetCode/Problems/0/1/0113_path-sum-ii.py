class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def traverse(node: Optional[TreeNode], curs: int, path: List[int]):
            nonlocal targetSum, result
            if not node:
                return

            curs += node.val

            path.append(node.val)
            if not node.left and not node.right and curs == targetSum:
                result.append(path[:])
            else:
                traverse(node.left, curs, path)
                traverse(node.right, curs, path)

            path.pop()

        traverse(root, 0, [])

        return result
