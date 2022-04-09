class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def preorder(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            return TreeNode(nums[mid], preorder(left, mid - 1), preorder(mid + 1, right))

        return preorder(0, len(nums) - 1)
