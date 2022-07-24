class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        smp, rmp = defaultdict(int), defaultdict(int)
        for rank, suit in zip(ranks, suits):
            smp[suit] += 1
            rmp[rank] += 1

        mxs, mxr = max(smp.values()), max(rmp.values())

        if mxs >= 5:
            return "Flush"
        elif mxr >= 3:
            return "Three of a Kind"
        elif mxr >= 2:
            return "Pair"

        return "High Card"
