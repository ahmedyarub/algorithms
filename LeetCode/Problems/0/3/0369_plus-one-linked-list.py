class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def traverse(node: ListNode) -> int:
            if not node:
                return 1

            carry, node.val = divmod(node.val + traverse(node.next), 10)

            return carry

        last_carry = traverse(head)

        if last_carry:
            new_node = ListNode()
            new_node.val = last_carry
            new_node.next = head
            head = new_node

        return head
