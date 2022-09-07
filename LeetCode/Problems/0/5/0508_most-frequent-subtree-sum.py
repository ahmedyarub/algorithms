class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnts, mx = Counter(), 0

        def dfs(node: Optional[TreeNode]):
            nonlocal mx
            if not node:
                return 0

            s = node.val + dfs(node.left) + dfs(node.right)
            cnts[s] += 1
            mx = max(mx, cnts[s])

            return s

        dfs(root)
        return [n for n, cnt in cnts.items() if cnt == mx]
