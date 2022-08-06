class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head, self.size = head, 0

        while head:
            head = head.next
            self.size += 1

    def getRandom(self) -> int:
        node = self.head
        for _ in range(randint(0, self.size - 1)):
            node = node.next

        return node.val
