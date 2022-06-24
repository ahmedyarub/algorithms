class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen, result = set(), set()

        def traverse(rem: List[int], path: tuple):
            if path not in seen:
                result.add(path)

                for i, num in enumerate(rem):
                    traverse(rem[:i] + rem[i + 1:], tuple(sorted((path + (num,)))))

        nums.sort()
        traverse(nums, ())
        return list(map(list, result))
