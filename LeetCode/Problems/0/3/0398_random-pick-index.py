class Solution:

    def __init__(self, nums: List[int]):
        self.mp = defaultdict(list)

        for i, num in enumerate(nums):
            self.mp[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.mp[target])
