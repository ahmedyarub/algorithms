class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.shuffled = nums[:]

    def reset(self) -> List[int]:
        self.shuffled = self.original[:]

        return self.shuffled

    def shuffle(self) -> List[int]:
        for i in range(len(self.original)):
            si = randrange(i, len(self.original))
            self.shuffled[i], self.shuffled[si] = self.shuffled[si], self.shuffled[i]

        return self.shuffled
