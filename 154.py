'''
154. Find Minimum in Rotated Sorted Array II
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return min(nums[0], nums[1])
        if sorted(nums)==nums:
            return nums[0]

        start = 0
        stop = len(nums)-1
        while stop-1>start:
            if nums[start]<nums[stop]:
                return nums[start]

            mid = (start + stop)//2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                stop = mid
            else:
                start+=1
        return min(nums[start], nums[stop])

a = Solution()
nums = [1, 1, 1,1, 2,0]
print(a.findMin(nums))
