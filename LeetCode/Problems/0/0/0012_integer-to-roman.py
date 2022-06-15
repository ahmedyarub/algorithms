class Solution:
    def intToRoman(self, num: int) -> str:
        digit, result, rn = 0, [], ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        while num:
            num, rem = divmod(num, 10)

            if 3 >= rem >= 1:
                result.append(rn[digit] * rem)
            elif rem == 4:
                result.append(rn[digit] + rn[digit + 1])
            elif 8 >= rem >= 5:
                result.append(rn[digit + 1] + rn[digit] * (rem - 5))
            elif rem == 9:
                result.append(rn[digit] + rn[digit + 2])
            digit += 2

        return "".join(reversed(result))
