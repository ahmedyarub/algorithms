class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(postorder[-1])

        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:len(postorder) - 1])

        return root
