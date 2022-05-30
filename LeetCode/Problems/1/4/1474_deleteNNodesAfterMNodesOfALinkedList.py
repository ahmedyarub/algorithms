class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current = head

        while current:
            for _ in range(m - 1):
                if current.next:
                    current = current.next
                else:
                    return head
            delete_current = current

            for _ in range(n):
                if delete_current.next:
                    delete_current = delete_current.next
                else:
                    current.next = None
                    return head
            current.next = delete_current.next
            current = current.next

        return head
