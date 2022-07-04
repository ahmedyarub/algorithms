class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr, self.cur = [], -1

        def traverse(node: Optional[TreeNode]):
            if node:
                traverse(node.left)
                self.arr.append(node.val)
                traverse(node.right)

        traverse(root)

    def next(self) -> int:
        self.cur += 1
        return self.arr[self.cur]

    def hasNext(self) -> bool:
        return self.cur + 1 < len(self.arr)
