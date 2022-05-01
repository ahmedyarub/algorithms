class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return min(letters, key=lambda x: ord(x) if ord(x) > ord(target) else float('inf'))
