class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stc = Counter(students)
        swi = 0

        while swi < len(sandwiches) and stc[sandwiches[swi]]:
            stc[sandwiches[swi]] -= 1
            swi += 1

        return sum(stc.values())
