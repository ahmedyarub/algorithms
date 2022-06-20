class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(reverse=True, key=len)

        pref, cnt = set(), 0

        for word in words:
            if word not in pref:
                cnt += len(word) + 1
                for i in range(len(word)):
                    pref.add(word[i:])

        return cnt
