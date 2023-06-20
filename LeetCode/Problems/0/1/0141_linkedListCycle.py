class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast, slow = head.next, head

        while fast and fast.next and slow and fast != slow:
            fast, slow = fast.next.next, slow.next

        return fast == slow
