class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []

        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                pairs = [nums1[i], nums2[j]]
                if len(ans) < k:
                    heappush(ans, [-(nums1[i] + nums2[j]), pairs])
                else:
                    if nums1[i] + nums2[j] > -ans[0][0]:
                        break
                    heappushpop(ans, [-(nums1[i] + nums2[j]), pairs])

        return list(map(lambda pair: pair[1], ans))
