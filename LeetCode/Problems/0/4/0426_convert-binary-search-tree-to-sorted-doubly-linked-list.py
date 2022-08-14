class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def treeToDoublyList(node: Optional[Node]) -> Tuple:
            head = node
            tail = head

            if node.left:
                lhead, ltail = treeToDoublyList(node.left)

                ltail.right = head
                head.left = ltail
                head = lhead

            if node.right:
                rhead, rtail = treeToDoublyList(node.right)

                tail.right = rhead
                rhead.left = tail
                tail = rtail

            return head, tail

        h, t = treeToDoublyList(root)

        h.left = t
        t.right = h

        return h
