class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)

        def dfs(node: Optional[TreeNode], col: int, level: int):
            if not node:
                return

            mp[col].append((level, node.val))

            dfs(node.left, col - 1, level + 1)
            dfs(node.right, col + 1, level + 1)

        dfs(root, 0, 0)

        return [list(map(lambda pair: pair[1], sorted(mp[k]))) for k in sorted(mp.keys())]
