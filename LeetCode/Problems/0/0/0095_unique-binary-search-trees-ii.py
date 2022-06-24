class Solution:
    def generateTrees(self, n):
        def generate_trees(start, end):
            return [TreeNode(i, l, r) for i in range(start, end + 1)
                    for l in generate_trees(start, i - 1)
                    for r in generate_trees(i + 1, end)] \
                if start <= end else [None, ]

        return generate_trees(1, n) if n else []
