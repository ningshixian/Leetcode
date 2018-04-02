'''
34. Search for a Range
这题要求在一个排好序可能有重复元素的数组里面找到包含某个值的区间范围。 要求使用O(log n)的时间，
所以我们采用两次二分查找。 

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        if not target in nums:
            return [-1,-1]
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                high = mid-1
            else:
                low = mid+1
        low2 = low
        high2 = len(nums)-1
        while low2<=high2:
            mid = (low2+high2)//2
            if nums[mid]<=target:
                low2 = mid+1
            else:
                high2 = mid-1
        return [low, high2]


a = Solution()
nums = [5, 7, 7, 8, 8,8,8,10]
target = 8
print(a.searchRange(nums, target))