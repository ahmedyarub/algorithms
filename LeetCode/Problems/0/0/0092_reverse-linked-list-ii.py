class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        cur, prev = head, None
        for _ in range(left - 1):
            prev = cur
            cur = cur.next

        right = right - left + 1

        tail, con = cur, prev

        for _ in range(right):
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = cur

        return head
