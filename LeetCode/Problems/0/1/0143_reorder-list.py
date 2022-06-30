class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cnt, stack, node = 0, [], head

        while node:
            stack.append(node)
            cnt += 1
            node = node.next

        for _ in range(cnt // 2):
            tmp = head.next
            nx = stack.pop()
            head.next = nx
            head.next.next = tmp
            head = tmp

        head.next = None
