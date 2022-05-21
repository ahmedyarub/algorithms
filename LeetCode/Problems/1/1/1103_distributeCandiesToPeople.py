class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result, i = [0] * num_people, 0

        while candies:
            gc = min(i + 1, candies)
            result[i % num_people] += gc
            i += 1
            candies -= gc

        return result
