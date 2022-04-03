class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0
        add = 1
        for i in reversed(range(len(digits))):
            s = digits[i] + add + carry
            digits[i] = s % 10
            carry = s // 10
            add = 0

            if not carry:
                break

        if carry:
            return [carry] + digits
        else:
            return digits
