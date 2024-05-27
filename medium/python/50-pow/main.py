class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive(x, n):
            if n == 0 or x == 1:
                return 1

            if n < 0:
                return 1 / recursive(x, -n)

            result = recursive(x * x, n // 2)

            return result * x if n & 1 else result

        return recursive(x, n)


# print(Solution().myPow(2, 10))
# print(Solution().myPow(2.1, 3))
# print(Solution().myPow(2, -2))
