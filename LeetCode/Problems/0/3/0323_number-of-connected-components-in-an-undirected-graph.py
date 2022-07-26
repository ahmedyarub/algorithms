class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = [-1] * n

        def add(fr: int, to: int):
            while ds[fr] != -1:
                fr = ds[fr]

            while ds[to] != -1:
                to = ds[to]

            if to != fr:
                ds[fr] = to

        for f, t in edges:
            add(f, t)

        return sum([p == -1 for p in ds])
