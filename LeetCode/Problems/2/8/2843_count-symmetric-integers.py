class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for n in range(low, high + 1):
            arr = []
            for k in str(n):
                arr.append(int(k))
            length = len(arr)
            if len(arr) > 0 and length % 2 == 0 and sum(arr[length // 2:]) == sum(arr[:length // 2]):
                ans += 1
        return ans
