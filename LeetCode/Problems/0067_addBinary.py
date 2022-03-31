class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        for i in range(max(len(a), len(b))):
            cur_sum = 0

            if i < len(a):
                cur_sum += int(a[len(a) - i - 1])

            if i < len(b):
                cur_sum += int(b[len(b) - i - 1])

            cur_sum += carry

            result = [str(cur_sum % 2)] + result
            carry = cur_sum // 2

        if carry:
            result = [str(carry)] + result

        return "".join(result)
