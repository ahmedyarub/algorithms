class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp, result = defaultdict(list), []

        for i, gs in enumerate(groupSizes):
            mp[gs].append(i)

            if len(mp[gs]) == gs:
                result.append([num for num in mp[gs]])
                mp[gs] = []

        return result
