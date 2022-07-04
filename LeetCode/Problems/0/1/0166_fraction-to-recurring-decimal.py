class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)

        div, rem = divmod(numerator, denominator)
        result = [str(div), '.']

        dd, mp = 0, dict()
        while rem:
            rem *= 10
            div, rem = divmod(rem, denominator)

            tpl = tuple((div, rem))
            if tpl in mp:
                result = result[:mp[tpl] + 2] + ['('] + result[mp[tpl] + 2:] + [')']
                break
            else:
                mp[tpl] = dd

            if rem or div:
                result.append(str(div))

            dd += 1

        return "".join([sign] + (result if len(result) > 2 else result[:1]))
