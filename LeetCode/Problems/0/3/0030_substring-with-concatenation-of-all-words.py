class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        all_strs = "".join(words)
        all_cnt, i, cur_cnt, result = Counter(all_strs), len(all_strs), Counter(s[:len(all_strs)]), []
        all_words_cnt = Counter(words)

        while i <= len(s):
            if all_cnt == cur_cnt:
                start = i - len(all_strs)
                if Counter(
                        [s[j:j + len(words[0])] for j in range(start, start + len(all_strs), len(words[0]))]
                ) == all_words_cnt:
                    result.append(start)

            if i == len(s):
                break

            cur_cnt[s[i - len(all_strs)]] -= 1
            cur_cnt[s[i]] += 1

            i += 1

        return result
