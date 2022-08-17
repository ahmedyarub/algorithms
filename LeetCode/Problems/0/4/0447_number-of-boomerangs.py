class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for a, b in points:
            counter = defaultdict(int)
            for x, y in points:
                key = (x - a) ** 2 + (y - b) ** 2
                result += 2 * counter[key]
                counter[key] += 1

        return result
