class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        l_time, l_task, i_task = 0, 0, set()
        for i, t in logs:
            t_len = t - l_time
            if t_len > l_task:
                i_task = {i, }
                l_task = t_len
            elif t_len == l_task:
                i_task.add(i)

            l_time = t

        return min(i_task)
