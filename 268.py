'''
268. Missing Number
题目翻译: 从0到n之间取出n个不同的数， 找出漏掉的那个。 注意：你的算法应当具有线性的时间复杂度。
你能实现只占用常数额外空间复杂度的算法吗？
例子
For example, Given nums = [0, 1, 3] return 2
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        nums = sorted(nums)
        if not nums[0]==0:return 0
        nn = 0
        for i in range(1, len(nums)):
            if not nums[i]==nn+1:
                return i
            nn = nums[i]
        return len(nums)


a = Solution()
nums = [1]
print(a.missingNumber(nums))