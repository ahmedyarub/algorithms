class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0
        stack = [(l, 1) for l in nestedList]

        while stack:
            l, index = stack.pop()

            if l.isInteger():
                total += l.getInteger() * index
            else:
                for item in l.getList():
                    stack.append((item, index + 1))

        return total
