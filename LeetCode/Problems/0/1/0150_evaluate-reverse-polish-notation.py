class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.strip('-').isnumeric():
                stack.append(int(token))
            else:
                r, l = stack.pop(), stack.pop()

                match token:
                    case '+':
                        stack.append(l + r)
                    case '-':
                        stack.append(l - r)
                    case '*':
                        stack.append(l * r)
                    case '/':
                        stack.append(int(l / r))
                    case _:
                        return -1

        return stack[-1]
