class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        num_primes = len([x for x in primes if x <= n])  # cleaned up per comment
        return (factorial(num_primes) * factorial(n - num_primes)) % (10 ** 9 + 7)
