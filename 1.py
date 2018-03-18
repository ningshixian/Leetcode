'''
1. Two Sum
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

如果我们用两个for循环，
O(n2)的时间复杂度去求解的话， 很容易计算出来， 但这明显不是面试官需要的答案。

那么我们能不能用O(n)的时间复杂度去解这道题呢？很显然是可以的
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_dict = {}
        for i in range(len(nums)):
            if nums[i] not in diff_dict:
                diff = target-nums[i]
                diff_dict[diff] = i
            else:
                # print(nums[i], diff_dict)
                return [diff_dict[nums[i]], i]



a = Solution()
nums = [3,2,3]
target = 6
print(a.twoSum(nums, target))