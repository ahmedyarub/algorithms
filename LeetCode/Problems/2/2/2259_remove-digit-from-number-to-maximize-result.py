class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last_index = 0
        for i in range(1, len(number)):
            if number[i - 1] == digit:
                if int(number[i]) > int(number[i - 1]):
                    return number[:i - 1] + number[i:]
                else:
                    last_index = i - 1

        if number[-1] == digit:
            last_index = len(number) - 1

        return number[:last_index] + number[last_index + 1:]
