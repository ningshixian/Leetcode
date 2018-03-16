'''
80. Remove Duplicates from Sorted Array II
同26题，同样是移除重复的元素， 但是可以允许最多两次重复元素存在。

For example, Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3]
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        j,counter=0,0
        for i in range(1, len(nums)):
            if nums[i]==nums[j]:
                counter+=1
                if counter<2:
                    j+=1
                    nums[j]=nums[i]
            else:
                j+=1
                nums[j]=nums[i]
                counter=0
        return j+1
                

        # if not nums: 
        #     return 0
        # if len(nums)==1:
        #     return 1
        # if len(nums)==2:
        #     return 2
        # i=0
        # j=i+1
        # while j<len(nums):
        #     if not nums[i]==nums[j]:
        #         nums[i+1]=nums[j]
        #         i+=1
        #         j+=1
        #     else:
        #         nums[i+1]=nums[j]
        #         i+=1
        #         while j+1<len(nums) and nums[j]==nums[j+1]:
        #             j+=1
        #         j+=1
        # return i+1

a = Solution()
nums = [1,1,1,2,2]
print(a.removeDuplicates(nums))