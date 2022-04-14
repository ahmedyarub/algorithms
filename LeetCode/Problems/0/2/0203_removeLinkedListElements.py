class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        node = head

        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return head
