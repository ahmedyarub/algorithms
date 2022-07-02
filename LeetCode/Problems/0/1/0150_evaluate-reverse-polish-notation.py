class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    r, l = stack.pop(), stack.pop()
                    stack.append(l - r)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    r, l = stack.pop(), stack.pop()
                    stack.append(int(l / r))
                case _:
                    stack.append(int(t))

        return stack.pop()
