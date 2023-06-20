class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1

            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        inorder_index_map, preorder_index = {v: i for i, v in enumerate(inorder)}, 0

        return array_to_tree(0, len(preorder) - 1)
