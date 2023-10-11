class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        dic, heap, i = {}, [], 0
        for person in sorted(people):
            while i < len(flowers) and flowers[i][0] <= person:
                heappush(heap, flowers[i][1])
                i += 1

            while heap and heap[0] < person:
                heappop(heap)

            dic[person] = len(heap)

        return [dic[person] for person in people]
