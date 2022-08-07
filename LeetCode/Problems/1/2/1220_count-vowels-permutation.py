class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @cache
        def perm(prev: str, level: int) -> int:
            nonlocal n
            if level == n:
                return 1

            match prev:
                case 'a':
                    chrs = ['e']
                case 'e':
                    chrs = ['a', 'i']
                case 'i':
                    chrs = ['a', 'e', 'o', 'u']
                case 'o':
                    chrs = ['i', 'u']
                case 'u':
                    chrs = ['a']
                case _:
                    chrs = ['a', 'e', 'i', 'o', 'u']

            return sum([perm(chr, level + 1) for chr in chrs]) % 1000000007

        return perm('', 0)
