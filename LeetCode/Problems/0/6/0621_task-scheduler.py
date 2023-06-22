class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = 0, Counter(tasks)
        by_size = sorted([[cnt[key], key] for key in cnt.keys()], reverse=True)

        idle = (by_size[0][0] - 1) * n

        for f, _ in by_size[1:]:
            idle -= min(by_size[0][0] - 1, f)
            if idle <= 0:
                return len(tasks)

        return len(tasks) + idle
