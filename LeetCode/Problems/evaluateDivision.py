from typing import List


class Solution:
    def createPairs(self, equations_values, variable, visited):
        return list(map(
            lambda pair: pair if pair[0][0] == variable else [[pair[0][1], pair[0][0]], 1 / pair[1]],
            list(filter(lambda pair: pair[0][0] == variable or pair[0][1] == variable, equations_values))))

    def evalQuery(self, equations_values, query, visited_pairs):
        new_equations_values = list(filter(lambda equation: equation[0] not in visited_pairs, equations_values))

        x_pairs = self.createPairs(new_equations_values, query[0], visited_pairs)

        similar_pairs = list(
            filter(lambda pair: pair[0][0] == query[0] and pair[0][1] == query[1], x_pairs))

        if len(similar_pairs) > 0:
            return similar_pairs[0][1]

        for x_pair in x_pairs:
            new_visited = visited_pairs.copy()
            new_visited.append(x_pair[0])

            y_val = self.evalQuery(new_equations_values, [query[1], x_pair[0][1]], new_visited)

            if y_val != -1:
                return x_pair[1] / y_val

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        solutions = []

        for query in queries:
            solutions.append(self.evalQuery(list(zip(equations, values)), query, []))

        return solutions


if __name__ == '__main__':
    print(Solution().calcEquation([["a", "b"], ["b", "c"]],
                                  [2.0, 3.0],
                                  [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
