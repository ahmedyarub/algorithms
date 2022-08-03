class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal mp
            if not node:
                return 0

            cur_depth = max(dfs(node.left), dfs(node.right)) + 1
            mp[cur_depth].append(node.val)

            return cur_depth

        result = []
        for d in range(1, dfs(root) + 1):
            result.append(mp[d])

        return result
