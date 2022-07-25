class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        queue = [1]
        while n > 1:
            n -= 1
            num = heappop(queue)
            for prime in primes:
                heappush(queue, prime * num)
                if num % prime == 0:
                    break
        return queue[0]
