class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = 0
        carry = 0
        max_len = max(len(num1), (len(num2)))
        for i in range(max_len):
            cur_sum = carry

            if i < len(num1):
                cur_sum += ord(num1[len(num1) - i - 1]) - ord('0')

            if i < len(num2):
                cur_sum += ord(num2[len(num2) - i - 1]) - ord('0')

            carry = cur_sum // 10
            result += (cur_sum % 10) * (10 ** i)

        return str(result + carry * (10 ** max_len))


if __name__ == '__main__':
    print(Solution().addStrings("1", "9"))
