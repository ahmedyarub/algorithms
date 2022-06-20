class Solution:
    def permute(self, nums):
        result = []

        def dfs(nums, path, res):
            nonlocal result

            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        dfs(nums, [], result)
        return result
