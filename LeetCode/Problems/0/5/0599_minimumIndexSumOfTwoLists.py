class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {r1: i1 for i1, r1 in enumerate(list1)}
        mn, result = float('inf'), []

        for i2, r2 in enumerate(list2):
            if r2 in m1:
                s = i2 + m1[r2]
                if s < mn:
                    mn = s
                    result = [r2]
                elif s == mn:
                    result.append(r2)

        return result
