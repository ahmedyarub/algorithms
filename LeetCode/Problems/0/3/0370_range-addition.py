class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length

        mps = defaultdict(defaultdict)
        for i, j, inc in updates:
            if j not in mps[i]:
                mps[i][j] = inc
            else:
                mps[i][j] += inc

        for start in mps:
            for end in mps[start]:
                for k in range(start, end + 1):
                    arr[k] += mps[start][end]

        return arr
