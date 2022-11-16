class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ns, result = set(), -1

        for num in nums:
            ns.add(num)

            if abs(num) > result and num * -1 in ns:
                result = abs(num)

        return result
