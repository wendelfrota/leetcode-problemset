class Solution(object):
    def twoSum(self, nums, target):
        index = {}

        for i, num in enumerate(nums):
            j = target - num
            if j in index:
                return [index[j], i]
            index[num] = i


# print(Solution().twoSum([2, 7, 11, 15], 9))
# print(Solution().twoSum([3, 2, 4], 6))
# print(Solution().twoSum([3,3], 6))
