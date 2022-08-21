class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if stamp == target:
            return [0]

        stamp, target = list(stamp), list(target)
        slen, tlen = len(stamp), len(target) - len(stamp) + 1
        ans, tdiff, sdiff = [], True, True

        while tdiff:
            tdiff = False
            for i in range(tlen):
                if all(target[i + j] == stamp[j] or target[i + j] == '*' for j in range(slen)) \
                        and any(target[i + j] != '*' for j in range(slen)):
                    tdiff = True
                    target = target[:i] + ['*'] * slen + target[i + slen:]
                    ans.append(i)

        return list(reversed(ans)) if all(t == '*' for t in target) else []
