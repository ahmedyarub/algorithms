class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for _, i in sorted(list(zip(heights, range(len(heights)))), reverse=True)]
