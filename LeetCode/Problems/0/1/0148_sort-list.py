class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rhead = slow.next
        slow.next = None

        lhead = self.sortList(head)
        rhead = self.sortList(rhead)

        if not lhead or not rhead:
            return lhead or rhead

        dummy = p = ListNode(0)

        while lhead and rhead:
            if lhead.val < rhead.val:
                p.next = lhead
                lhead = lhead.next
            else:
                p.next = rhead
                rhead = rhead.next

            p = p.next

        p.next = lhead or rhead

        return dummy.next
