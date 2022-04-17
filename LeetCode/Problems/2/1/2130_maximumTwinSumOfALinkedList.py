class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        deq = deque()

        while head:
            deq.append(head.val)
            head = head.next

        result = 0

        while deq:
            result = max(result, deq.pop() + deq.popleft())

        return result
