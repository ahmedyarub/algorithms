class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_counts = Counter(magazine)

        for c in ransomNote:
            if c in m_counts and m_counts[c] > 0:
                m_counts[c] -= 1
            else:
                return False

        return True
