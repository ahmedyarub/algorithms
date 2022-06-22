class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i1, i2 = 0, 0
        slots1.sort()
        slots2.sort()
        while i1 < len(slots1) and i2 < len(slots2):
            if slots1[i1][1] > slots2[i2][0] and slots1[i1][0] < slots2[i2][1]:
                common_from = max(slots1[i1][0], slots2[i2][0])
                if min(slots1[i1][1], slots2[i2][1]) - common_from >= duration:
                    return [common_from, common_from + duration]

            if slots1[i1][1] > slots2[i2][1]:
                i2 += 1
            else:
                i1 += 1
        return []
