class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        result, cur_path = [], []

        def driver(node: Optional[TreeNode], cur_sum: int):
            nonlocal result

            if not node:
                return

            s = cur_sum + node.val
            cur_path.append(node.val)
            if s == targetSum and not node.left and not node.right:
                result.append(cur_path[:])
            else:
                driver(node.left, s)
                driver(node.right, s)

            cur_path.pop()

            return

        driver(root, 0)
        return result
