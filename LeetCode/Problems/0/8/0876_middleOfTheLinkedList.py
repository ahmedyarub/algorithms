class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while True:
            if not fast.next:
                return slow
            elif not fast.next.next:
                return slow.next
            else:
                fast, slow = fast.next.next, slow.next
