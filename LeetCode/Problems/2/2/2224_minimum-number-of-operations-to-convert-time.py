class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = 60 * int(current[:2]) + int(current[3:])
        correct = 60 * int(correct[:2]) + int(correct[3:])
        diff = correct - current
        return diff // 60 + (diff % 60) // 15 + ((diff % 60) % 15) // 5 + ((diff % 60) % 15) % 5
