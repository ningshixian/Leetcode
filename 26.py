'''
26. Remove Duplicates from Sorted Array
在一个排序好的数组里面删除重复的元素

For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        i=0
        j=i+1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
        return i+1

a = Solution()
nums = [1,1, 2]
print(a.removeDuplicates(nums))
