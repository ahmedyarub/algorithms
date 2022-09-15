class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []

        changed.sort()
        cnt, result = Counter(changed), []

        for num in [v for v in cnt.keys()]:
            if num % 2 or not cnt[num // 2]:
                if cnt[num] <= cnt[num * 2]:
                    result.extend([num] * (cnt[num] // (1 if num else 2)))
                    cnt[num * 2] -= cnt[num]
                    del cnt[num]
                else:
                    return []
            else:
                result.extend([num // 2] * (cnt[num // 2] // (1 if num else 2)))
                cnt[num] -= cnt[num // 2]
                del cnt[num // 2]

        return result
