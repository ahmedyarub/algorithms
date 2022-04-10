class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sorting_algorithm(log):
            left_side, right_side = log.split(" ", 1)

            if right_side[0].isalpha():
                return (0, right_side, left_side)
            else:
                return (1,)

        return sorted(logs, key=sorting_algorithm)
