class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set([city[1] for city in paths]) - set([city[0] for city in paths])).pop()
