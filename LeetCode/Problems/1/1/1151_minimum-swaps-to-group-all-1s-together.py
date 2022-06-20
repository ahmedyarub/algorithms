class Solution:
    def minSwaps(self, data: List[int]) -> int:
        cones = data.count(1)
        wones = data[:cones].count(1)
        mxones = wones
        for i in range(cones, len(data)):
            wones += (data[i] - data[i - cones])
            mxones = max(mxones, wones)

        return cones - mxones
