class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result, queue = [], [root] if root else []

        while queue:
            node = queue.pop(0)

            if not node:
                result.append('null')
            else:
                result.append(str(node.val))

                queue.extend([node.left, node.right])

        return '[' + ",".join(result) + ']'

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        arr = data[1:len(data) - 1].split(',')

        if not arr[0]:
            return None
        else:
            root = TreeNode(int(arr[0]))
            st = [root]
            i = 1

        while i < len(arr):
            parent = st.pop(0)

            if arr[i] != 'null':
                parent.left = TreeNode(arr[i])
                st.append(parent.left)

            if arr[i + 1] != 'null':
                parent.right = TreeNode(arr[i + 1])
                st.append(parent.right)

            i += 2

        return root
