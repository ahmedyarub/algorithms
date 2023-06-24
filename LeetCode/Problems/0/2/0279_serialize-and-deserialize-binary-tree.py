class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = []

        def preorder(node: Optional[TreeNode]):
            if not node:
                result.append("-2000")
            else:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)

        return ','.join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nums, i = data.split(','), 0

        def build() -> Optional[TreeNode]:
            nonlocal i
            val = int(nums[i])
            i += 1
            if val == -2000:
                return None
            else:
                node = TreeNode(val)
                node.left = build()
                node.right = build()

                return node

        return build()
