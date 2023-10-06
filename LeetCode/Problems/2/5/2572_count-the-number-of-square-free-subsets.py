class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        def count(arr):
            if not arr:
                return 1
            arr1 = [x for x in arr if math.gcd(x, arr[0]) == 1]

            return count(arr[1:]) + cnt[arr[0]] * count(arr1)

        candidates = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        return (count(candidates) * pow(2, cnt[1]) - 1) % (10 ** 9 + 7)
