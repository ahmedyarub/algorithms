class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sqs = [min(l, w) for l, w in rectangles]
        return Counter(sqs)[max(sqs)]
