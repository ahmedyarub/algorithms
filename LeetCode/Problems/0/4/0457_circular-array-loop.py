class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            visited = set()

            j = i
            while True:
                j = (j + nums[j])

                if j < 0:
                    j += len(nums)

                j %= len(nums)

                if abs(nums[i]) / nums[i] != abs(nums[j]) / nums[j]:
                    break

                if j == i:
                    if visited:
                        return True
                    else:
                        break
                elif j in visited:
                    break

                visited.add(j)

        return False
