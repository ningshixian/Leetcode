'''
153. Find Minimum in Rotated Sorted Array
这题要求在一个轮转了的排序数组里面找到最小值， 我们可以用二分法来做。

假设在一个轮转的排序数组A， 我们首先获取中间元素的值， A[mid]， mid = (start + stop) / 2。 
因为数组没有重复元素， 那么就有两种情况：
A[mid] > A[start]， 那么最小值一定在右半区间， 譬如[4,5,6,7,0,1,2]， 中间元素为7， 7 > 4， 最小元素
一定在[7,0,1,2]这边， 于是我们继续在这个区间查找。
A[mid] < A[start]， 那么最小值一定在左半区间， 譬如[7,0,1,2,4,5,6]， 这件元素为2， 2 < 7， 我们继续
在[7,0,1,2]这个区间查找。
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        if len(nums)==1 or sorted(nums)==nums:
            return nums[0]
        start = 0
        stop = len(nums)-1
        while stop>start:
            mid = (start + stop)//2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                stop = mid
            else:
                if nums[start] > nums[stop]:
                    return nums[stop]
                if nums[stop] > nums[start]:
                    return nums[start]



a = Solution()
nums = [1,2,3]
print(a.findMin(nums))