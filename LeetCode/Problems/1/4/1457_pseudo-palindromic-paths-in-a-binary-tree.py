class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        cnt, result = defaultdict(int), 0

        def backtrack(node: TreeNode):
            nonlocal result, cnt

            cnt[node.val] += 1

            if not (node.left or node.right):
                result += sum(v % 2 for v in cnt.values()) <= 1
            else:
                if node.left:
                    backtrack(node.left)
                if node.right:
                    backtrack(node.right)

            cnt[node.val] -= 1

        backtrack(root)

        return result
