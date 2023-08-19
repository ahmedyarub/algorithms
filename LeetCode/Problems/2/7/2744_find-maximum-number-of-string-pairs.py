class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        st, result = set(), 0

        for word in words:
            if word in st:
                st.remove(word)
                result += 1
            else:
                st.add(word[::-1])

        return result
