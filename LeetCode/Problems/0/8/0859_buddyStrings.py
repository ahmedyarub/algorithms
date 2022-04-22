class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        diffs = 0
        cs, cg = None, None
        counts = defaultdict(int)
        for a, b in zip(s, goal):
            counts[a] += 1
            if a != b:
                diffs += 1
                if diffs > 2:
                    return False
                elif diffs == 2:
                    if b != cs or a != cg:
                        return False
                else:
                    cs, cg = a, b

        return diffs == 2 or (not diffs and any(count >= 2 for count in counts.values()))
