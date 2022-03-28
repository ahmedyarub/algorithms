class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(root, result):
            if not root:
                return

            result.append(root.val)

            for child in root.children:
                dfs(child, result)

        dfs(root, result)

        return result
