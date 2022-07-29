class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head or not head.next or not head.next.next:
            return head

        tail, size = head, 1
        while tail.next:
            size += 1
            tail = tail.next

        onode = head
        for _ in range(size // 2):
            tmp = onode.next
            onode.next = tmp.next
            onode = onode.next
            tail.next = tmp
            tail = tail.next
            tail.next = None

        return head
