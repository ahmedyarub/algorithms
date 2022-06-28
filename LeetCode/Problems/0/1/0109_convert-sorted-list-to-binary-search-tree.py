class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        prev, slow, fast = head, head, head

        if not fast.next:
            return TreeNode(head.val)

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        return TreeNode(slow.val, self.sortedListToBST(head), self.sortedListToBST(slow.next))
