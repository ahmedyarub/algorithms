class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head
