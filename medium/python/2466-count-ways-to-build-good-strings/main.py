class Solution:
    MOD = 10**9 + 7

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        if zero > one:
            zero, one = one, zero
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        for i in range(1, high + 1):
            if i >= one:
                dp[i] = (dp[i - zero] + dp[i - one]) % self.MOD
            elif i >= zero:
                dp[i] = dp[i - zero] % self.MOD
            if i >= low:
                ans = (ans + dp[i]) % self.MOD
        return ans


# print(Solution().countGoodStrings(3, 3, 1, 1))
# print(Solution().countGoodStrings(2, 3, 1, 2))
