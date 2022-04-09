class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        deq = deque()

        cur_node = head
        while cur_node:
            deq.append(cur_node.val)
            cur_node = cur_node.next

        while deq:
            left = deq.popleft()

            if not deq:
                return True

            right = deq.pop()

            if left != right:
                return False

        return True
