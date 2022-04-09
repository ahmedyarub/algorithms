class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        pre = dict()

        for n2 in nums2:
            while stack and n2 > stack[-1]:
                pre[stack.pop()] = n2

            stack.append(n2)

        return [pre.get(n1, -1) for n1 in nums1]
