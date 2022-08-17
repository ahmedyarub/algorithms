class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2 = [], []

        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        result, carry = None, 0
        while st1 or st2:
            node = ListNode((st1.pop() if st1 else 0) + (st2.pop() if st2 else 0) + carry)
            carry, node.val = divmod(node.val, 10)
            node.next = result
            result = node

        if carry:
            node = ListNode(carry)
            node.next = result
            result = node

        return result
