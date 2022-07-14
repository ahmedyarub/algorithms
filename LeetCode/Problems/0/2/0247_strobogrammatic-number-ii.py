class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return ["".join(
            list(prd) + [c] + list(reversed(list(map({'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}.get, prd)))))
                for prd in product(['0', '1', '6', '8', '9'], repeat=n // 2)
                for c in (['0', '1', '8'] if n % 2 else ['']) if not prd or prd[0] != '0']
