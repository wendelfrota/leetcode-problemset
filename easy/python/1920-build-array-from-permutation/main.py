class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans


# print(Solution().buildArray([0, 2, 1, 5, 3, 4]))
# print(Solution().buildArray([5, 0, 1, 2, 3, 4]))
