class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur, length = head, 0

        while cur:
            cur = cur.next
            length += 1

        width, remainder = divmod(length, k)

        ans, cur = [], head
        for i in range(k):
            ans.append(cur)
            for j in range(width + (i < remainder) - 1):
                cur = cur.next

            if cur:
                cur.next, cur = None, cur.next

        return ans
