class Solution: 
    def captureForts(self, forts: List[int]) -> int:
        ans = ii = 0 
        for i, x in enumerate(forts): 
            if x: 
                if forts[ii] == -x:
                    ans = max(ans, i-ii-1)
                ii = i 
        return ans 