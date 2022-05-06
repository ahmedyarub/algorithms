class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([c for c in sentence])) == 26
