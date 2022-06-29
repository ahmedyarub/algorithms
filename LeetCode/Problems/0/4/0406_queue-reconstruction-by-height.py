class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))

        result = [None] * len(people)

        for i, p in enumerate(people):
            for j in range(i, p[1], -1):
                result[j] = result[j - 1]

            result[p[1]] = p

        return result
