class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode(0)]
        return [TreeNode(left=subTree1, right=subTree2, val=0)
                for i in range(1, n - 1)
                for subTree1 in self.allPossibleFBT(i)
                for subTree2 in self.allPossibleFBT(n - 1 - i)]
