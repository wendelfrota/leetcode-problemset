class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return False if num % 10 == 0 and num != 0 else True


# print(Solution().isSameAfterReversals(526))
# print(Solution().isSameAfterReversals(1800))
# print(Solution().isSameAfterReversals(0))
