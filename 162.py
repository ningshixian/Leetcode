'''
162. Find Peak Element
这题要求我们在一个无序的数组里面找到一个peak元素， 所谓peak， 就是值比两边邻居大就行了。
对于这题， 最简单地解法就是遍历数组， 只要找到第一个元素， 大于两边就可以了， 复杂度为O(N)。 但这
题还可以通过二分来做
'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        idx = 0
        m = nums[0]
        for i in range(len(nums)):
            if nums[i]>m:
                m=nums[i]
                idx = i
        return idx


a = Solution()
nums = [1,3,2,1,6]
print(a.findPeakElement(nums))