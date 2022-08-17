class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            parent = None
            target = root
            root = root.right if root.right else root.left
            queue = []
        else:
            queue = [root]
            target = None
            parent = None

        left = None
        while queue:
            node = queue.pop()

            if node.left:
                if node.left.val == key:
                    parent = node
                    target = node.left
                    left = True
                    break

                queue.append(node.left)
            if node.right:
                if node.right.val == key:
                    parent = node
                    target = node.right
                    left = False
                    break

                queue.append(node.right)

        if target:
            if target.right:
                if target.right.left:
                    if target.left:
                        node = target.left

                        while node.right:
                            node = node.right

                        node.right = target.right.left
                    else:
                        target.left = target.right.left

                target.right.left = target.left
                nxt = target.right
            else:
                nxt = target.left

            if parent:
                if left:
                    parent.left = nxt
                else:
                    parent.right = nxt

        return root
