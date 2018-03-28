'''
665. Non-decreasing Array
判断给定List是否可以通过改变其中的一个值，使得List顺序排序

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
'''
class Solution(object):
	def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return 
        if len(nums)==1:
            return True
        if len(nums)==2:
            return True
        
        def compair(a, b):
            count=0
            for i in range(len(a)):
                if not a[i]==b[i]:
                    count+=1
            return count
        
        last = 0
        for i in range(len(nums)):
            if i+1 < len(nums):
                if nums[i]<=nums[i+1]:
                    pass
                else:
                    temp = nums[:]
                    nums[i+1] = nums[i]
                    new = sorted(nums)
                    temp[i]=temp[i+1]
                    new2=sorted(temp)
                    if compair(nums, new)<=1 or compair(temp, new2)<=1:
                        return True
                    else:
                        return False
        return True


a = Solution()
nums = 
print()