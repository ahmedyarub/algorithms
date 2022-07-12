class Solution:
    def calculate(self, s: str) -> int:
        nums, ops, i = [], [], 0
        while i < len(s):
            if ord('9') >= ord(s[i]) >= ord('0'):
                j = i + 1

                while j < len(s) and ord('9') >= ord(s[j]) >= ord('0'):
                    j += 1

                nums.append(int(s[i:j]))
                i = j

                while ops and ops[-1] in ['*', '/']:
                    r = nums.pop()
                    l = nums.pop()
                    op = ops.pop()
                    nums.append((l * r) if op == '*' else (l // r))

            if i < len(s) and s[i] != ' ':
                ops.append(s[i])

            i += 1

        while ops:
            l = nums.pop(0)
            r = nums.pop(0)
            op = ops.pop(0)
            nums.insert(0, (l + r) if op == '+' else (l - r))

        return nums.pop()
