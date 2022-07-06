class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            curi, prev = start, nums[start]
            while True:
                nexti = (curi + k) % n
                nums[nexti], prev = prev, nums[nexti]
                curi = nexti
                count += 1

                if start == curi:
                    break
            start += 1
