class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        while head:
            result = ListNode(head.val, result)
            head = head.next

        return result
