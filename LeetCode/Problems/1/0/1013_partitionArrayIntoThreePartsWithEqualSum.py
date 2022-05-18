class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0: return False
        count, cumsum, target = 0, 0, total // 3
        for num in arr:
            cumsum += num
            if cumsum == target:
                cumsum = 0
                count += 1
        return count >= 3
