class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        curl, curs = 0, 0
        queue = [[root, 0]]

        while queue:
            node, level = queue.pop(0)

            if level != curl:
                curl = level
                curs = 0

            curs += node.val

            if node.left:
                queue.append([node.left, curl + 1])

            if node.right:
                queue.append([node.right, curl + 1])

        return curs
