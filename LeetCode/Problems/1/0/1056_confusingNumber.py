class Solution:
    def confusingNumber(self, n: int) -> bool:
        return all([c in {'0', '1', '6', '8', '9'} for c in str(n)]) and \
            n != int("".join(reversed(list(map(lambda n: str({0: 0, 1: 1, 6: 9, 8: 8, 9: 6}.get(n, 0)), [int(c) for c in str(n)])))))