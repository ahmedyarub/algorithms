class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        heads, headl, small, large, node = None, None, None, None, head

        while node:
            if node.val < x:
                if not heads:
                    heads = node
                    small = node
                else:
                    small.next = node
                    small = node
            elif node.val >= x:
                if not headl:
                    headl = node
                    large = node
                else:
                    large.next = node
                    large = node
            tmp = node.next
            node.next = None
            node = tmp
        if small:
            small.next = headl
            return heads
        else:
            return headl
