class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not (head and head.next and k):
            return head

        nt, node = head, head

        ln = 0
        while node:
            ln += 1
            node = node.next

        k %= ln

        if not k:
            return head

        node = head
        for _ in range(k):
            node = node.next

        while node.next:
            node = node.next
            nt = nt.next

        nh = nt.next
        nt.next = None
        node.next = head

        return nh
