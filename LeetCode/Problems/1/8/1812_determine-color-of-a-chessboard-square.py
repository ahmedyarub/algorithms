class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + ord(coordinates[1]) - ord('1')) % 2
