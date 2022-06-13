class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        running = brackets[0][0]
        for i in range(0, len(brackets)):
            if i != 0:
                running = brackets[i][0] - brackets[i - 1][0]
            if income == 0:
                break
            elif income > running:
                tax = tax + (running * (brackets[i][1] / 100))
                income = income - running
            else:
                tax = tax + (income * (brackets[i][1] / 100))
                income = 0
        return tax
