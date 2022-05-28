class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_counts = Counter([sum([int(c) for c in str(i)]) for i in range(1, n + 1)])
        max_sum = max(sum_counts.values())
        return Counter(sum_counts.values())[max_sum]
