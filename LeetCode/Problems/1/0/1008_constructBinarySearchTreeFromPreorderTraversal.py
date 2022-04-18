class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for v in preorder[1:]:
            node = TreeNode(v)
            if node.val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and node.val > stack[-1].val:
                    l = stack.pop()
                l.right = node
            stack.append(node)
        return root
