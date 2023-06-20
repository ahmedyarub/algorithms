class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cntp, cnts, results, i = Counter(p), Counter(s[:len(p)]), [], len(p) - 1

        while True:
            if all([key in cnts.keys() and cntp[key] == cnts[key] for key in cntp.keys()]):
                results.append(i - len(p) + 1)

            i += 1
            if i >= len(s):
                return results

            if s[i] not in cnts:
                cnts[s[i]] = 1
            else:
                cnts[s[i]] += 1

            cnts[s[i - len(p)]] -= 1
