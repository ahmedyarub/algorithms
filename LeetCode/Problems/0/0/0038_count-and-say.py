class Solution:
    def countAndSay(self, n: int) -> str:
        term, result = 1, '1'

        for _ in range(n - 1):
            prev, cnt, nxt = result[0], 1, []
            for d in result[1:] + '*':
                if d != prev:
                    nxt.append(str(cnt) + prev)
                    prev = d
                    cnt = 1
                else:
                    cnt += 1

            result = "".join(nxt)

        return result
