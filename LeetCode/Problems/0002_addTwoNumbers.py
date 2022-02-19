class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur_node = root = ListNode()

        while True:
            v1 = 0 if l1 is None else l1.val
            v2 = 0 if l2 is None else l2.val

            carry, cur_node.val = divmod(v1 + v2 + carry, 10)

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

            if not l1 and not l2:
                break

            cur_node.next = ListNode()
            cur_node = cur_node.next

        if carry != 0:
            cur_node.next = ListNode(carry)

        return root
