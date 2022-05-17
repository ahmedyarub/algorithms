class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]

        while True:
            node = queue.pop()

            if node.val == target.val:
                return node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
