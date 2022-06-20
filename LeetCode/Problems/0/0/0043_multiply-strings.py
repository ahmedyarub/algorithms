class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result, num1, num2 = [0] * (len(num1) + len(num2)), num1[::-1], num2[::-1]
        for i in range(len(num1)):
            carry = 0
            for j in range(len(num2)):
                carry, mul = divmod(int(num1[i]) * int(num2[j]) + carry + result[i + j], 10)
                result[i + j] = mul

            k = i + len(num2)
            while carry:
                carry, add = divmod(result[k] + carry, 10)
                result[k] += add

        for i in reversed(range(len(result))):
            if result[i] != 0:
                return "".join(map(str, reversed(result[:i + 1])))

        return "0"
