class Solution:
    def isPossible(self, target: List[int]) -> bool:

        if len(target) == 1:
            return target == [1]

        total_sum = sum(target)

        target = [-num for num in target]
        heapq.heapify(target)
        while -target[0] > 1:
            largest = -target[0]
            rest = total_sum - largest

            if rest == 1:
                return True

            x = largest % rest

            if x == 0 or x == largest:
                return False

            heapq.heapreplace(target, -x)
            total_sum = total_sum - largest + x

        return True
