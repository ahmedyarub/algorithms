class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node, nh = head, head

        for _ in range(n):
            node = node.next

        if node:
            while node.next:
                node = node.next
                nh = nh.next
        else:
            return head.next

        if nh.next:
            nh.next = nh.next.next

        return head
