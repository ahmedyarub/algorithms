class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def factors(start: int, num: int) -> List[List[int]]:
            fs = set()

            for f in range(start, int(num ** 0.5) + 1):
                if not num % f:
                    for fc in factors(f, num // f):
                        fs.add(tuple(sorted([f] + fc)))

                    fs.add(tuple(sorted([f, num // f])))

            if not fs:
                if n > num > 0:
                    return [[num]]
                else:
                    return []
            else:
                return list(map(list, fs))

        return factors(2, n)
