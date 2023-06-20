class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result, dict = [], defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1

            dict[tuple(cnt)].append(s)

        return [words for words in dict.values()]
