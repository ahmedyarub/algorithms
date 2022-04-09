class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ps = dict()
        sp = dict()

        words = s.split()

        if len(words) != len(pattern):
            return False

        for p, w in zip(pattern, words):
            if p not in ps:
                if w in sp:
                    return False

                ps[p], sp[w] = w, p
            elif sp.get(w) != p:
                return False

        return True
