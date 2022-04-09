class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and temperatures[cur_day] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = cur_day - prev_day

            stack.append(cur_day)

        return result
