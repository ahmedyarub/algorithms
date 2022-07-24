class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(index: int, tree: List[int]):
            index += size

            tree[index] += 1
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]

        def query(right: int, tree: List[int]) -> int:
            qresult = 0
            left = size
            right += size
            while left < right:
                if left % 2 == 1:
                    qresult += tree[left]
                    left += 1

                left //= 2

                if right % 2 == 1:
                    right -= 1
                    qresult += tree[right]

                right //= 2
            return qresult

        offset = 10 ** 4
        size = 2 * 10 ** 4 + 1
        tree = [0] * (2 * size)
        result = []
        for num in reversed(nums):
            smaller_count = query(num + offset, tree)
            result.append(smaller_count)
            update(num + offset, tree)

        return list(reversed(result))
