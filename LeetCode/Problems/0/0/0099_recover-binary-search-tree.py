from typing import Optional

from Utils.treeviz import TreeNode, stringToTree, drawtree


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def traverse(node: Optional[TreeNode]) -> tuple:
            mns, mxs = [],[]

            for nxt in [node.left,node.right]:
                if nxt:
                    lres = traverse(nxt)
                    mns.append(lres[0])
                    mxs.append(lres[1])

            

        traverse(root, TreeNode(float('-inf')), TreeNode(float('inf')))


if __name__ == '__main__':
    root = stringToTree('[2,3,1]')
    drawtree(root)
    print(Solution().recoverTree(root))
    # print(Solution().recoverTree(stringToTree('[1,3,null,null,2]')))
    # print(Solution().recoverTree(stringToTree('[3,1,4,null,null,2]')))
