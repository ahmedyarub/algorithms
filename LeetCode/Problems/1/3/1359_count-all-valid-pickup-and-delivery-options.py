class Solution:
    def countOrders(self, n: int) -> int:
        @cache
        def dp(unpicked: int, undelivered: int) -> int:
            if not unpicked and not undelivered:
                return 1

            if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
                return 0

            return (
                    (unpicked * dp(unpicked - 1, undelivered) + (undelivered - unpicked) * dp(unpicked, undelivered - 1)
                     )
                    % (pow(10, 9) + 7))

        return dp(n, n)
