class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ln, step = len(code), 1 if k >= 0 else -1
        code.extend(code + code)

        return [sum(code[i + step:i + k + step:step]) for i in range(ln, 2 * ln)]
