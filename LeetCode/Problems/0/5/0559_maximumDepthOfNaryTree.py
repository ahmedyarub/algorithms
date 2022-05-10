def maxDepth(self, root: 'Node') -> int:
    def traverse(node, depth):
        if not node:
            return depth
        elif not node.children:
            return depth + 1

        return max([traverse(child, depth + 1) for child in node.children])

    return traverse(root, 0)
