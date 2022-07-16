class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower, stack = -float('inf'), []

        for curr in preorder:
            if curr <= lower:
                return False

            while stack and curr > stack[-1]:
                lower = stack.pop()

            stack.append(curr)

        return True
