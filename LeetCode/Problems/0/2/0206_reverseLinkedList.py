class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nxt, head.next = head.next, None

        while nxt:
            nxt.next, head, nxt = head, nxt, nxt.next

        return head
