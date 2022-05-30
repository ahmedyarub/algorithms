class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        queue, result = [root], []

        while queue:
            node = queue.pop()

            if node.left:
                queue.append(node.left)
                if not node.right:
                    result.append(node.left.val)

            if node.right:
                queue.append(node.right)
                if not node.left:
                    result.append(node.right.val)

        return result
