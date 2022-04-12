class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head
