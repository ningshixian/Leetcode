'''
27. Remove Element
在一个数组里面移除指定value， 并且返回新的数组长度。
这题唯一需要注意的地方在于 in place ， 不能新建另一个数组。
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,j=0,0
        while j<len(nums):
            if nums[j]==val:
                j+=1
            else:
                nums[i]=nums[j]
                i+=1
                j+=1
        return i

a = Solution()
nums = [4,3]
val = 3
print(a.removeElement(nums, val))