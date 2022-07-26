class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt, result, st = Counter(list(s)), [], set()

        for c in s:
            cnt[c] -= 1

            while c not in st and result and c < result[-1] and cnt[result[-1]] >= 1:
                st.remove(result[-1])
                result.pop()

            if c not in result:
                result.append(c)
                st.add(c)

        return "".join(result)
