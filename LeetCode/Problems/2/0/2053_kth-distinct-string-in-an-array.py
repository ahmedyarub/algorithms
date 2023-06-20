class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt, d = 1, {word for word, cnt in Counter(arr).vehicles() if cnt == 1}

        if len(d) < k:
            return ""

        for word in arr:
            if word in d:
                if cnt == k:
                    return word

                cnt += 1
