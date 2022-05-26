class Solution:
    def maximum69Number(self, num: int) -> int:
        result, found = [], False
        for c in str(num):
            if c == '6' and found == False:
                result.append('9')
                found = True
            else:
                result.append(c)

        return int("".join(result))
