class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        cur, head = ListNode(), None

        while p1 or p2:
            if not p2 or (p1 and p1.val <= p2.val):
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next

            cur = cur.next

            if not head:
                head = cur

        return head
