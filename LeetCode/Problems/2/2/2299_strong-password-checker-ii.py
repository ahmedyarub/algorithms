class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        oneUpper, oneLower, oneDigit, oneSpl = False, False, False, False

        if len(password) < 8:
            return False
        for idx, p in enumerate(password):
            if p.isupper():
                oneUpper = True
            if p.islower():
                oneLower = True
            if p.isdigit():
                oneDigit = True
            if p in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']:
                oneSpl = True
            if idx < len(password) - 1:
                if password[idx] == password[idx + 1]:
                    return False

        return oneUpper and oneSpl and oneDigit and oneLower
