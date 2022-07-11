from typing import Optional

from Utils.treeviz import TreeNode, stringToTree


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(node: Optional[TreeNode]):
            d = 0
            while node:
                d += 1
                node = node.left

            return d

        def exists(idx: int, cur: int, node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            elif idx == cur:
                return True

        return depth(root)


if __name__ == '__main__':
    print(Solution().countNodes(stringToTree('[1,2,3,4,5,6]')))
    print(Solution().countNodes(None))
    print(Solution().countNodes(stringToTree('[1]')))
