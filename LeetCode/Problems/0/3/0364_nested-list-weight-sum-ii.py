class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        maximum = 1
        res = 0
        total = 0

        def dfs(depth: int, ls):
            nonlocal maximum, res, total
            for nested in ls:
                if depth > maximum:
                    res += (depth - maximum) * total
                    maximum = depth
                if nested.isInteger():
                    num = nested.getInteger()
                    total += num
                    res += (maximum - depth + 1) * num
                else:
                    dfs(depth + 1, nested.getList())

        dfs(1, nestedList)
        return res
