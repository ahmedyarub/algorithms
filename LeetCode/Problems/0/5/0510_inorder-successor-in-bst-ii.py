class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            node = node.right
            while node.left:
                node = node.left

            return node
        else:
            while node.parent and node.parent.left != node:
                node = node.parent

            return node.parent
