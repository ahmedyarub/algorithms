class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}
        for i, num in enumerate(nums):
            cur_bucket = num // (t + 1)

            if cur_bucket in buckets or \
                    (cur_bucket - 1 in buckets and num - buckets[cur_bucket - 1] <= t) or \
                    (cur_bucket + 1 in buckets and buckets[cur_bucket + 1] - num <= t):
                return True

            buckets[cur_bucket] = num
            if len(buckets) > k:
                del buckets[nums[i - k] // (t + 1)]

        return False
