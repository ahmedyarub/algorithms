class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if not flowerbed[i]:
                if (not i or not flowerbed[i - 1]) and ((i == len(flowerbed) - 1) or (not flowerbed[i + 1])):
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n
