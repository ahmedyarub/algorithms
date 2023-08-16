from typing import Optional


class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        result, cnt = '', 0

        def traverse(node: object):
            nonlocal result, cnt

            if result:
                return

            if node.len:
                if node.left:
                    traverse(node.left)

                if node.right:
                    traverse(node.right)
            else:
                if cnt + len(node.val) >= k:
                    result = node.val[k - cnt - 1:k - cnt]
                else:
                    cnt += len(node.val)

        traverse(root)

        return result
