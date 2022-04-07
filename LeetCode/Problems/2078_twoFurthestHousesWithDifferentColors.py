class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r = 0, len(colors) - 1
        dist = 0

        while r > l:
            if colors[r] != colors[l]:
                dist = r - l
                break
            r -= 1

        l, r = 0, len(colors) - 1
        while r > l:
            if colors[r] != colors[l]:
                dist = max(dist, r - l)
                break
            l += 1

        return dist
