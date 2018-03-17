'''
88. Merge Sorted Array
A和B都已经是排好序的数组， 我们只需要从后往前比较就可以了。
因为A有足够的空间容纳A + B， 我们使用游标i指向m + n - 1， 也就是最大数值存放的地方， 从后往前遍历
A， B， 谁大就放到i这里， 同时递减i。
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 and not nums2:
            return
        i = m-1
        j = n-1
        k = n+m-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while i>=0:
            nums1[k]=nums1[i]
            i-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1


a = Solution()
print(a.merge([1], 1, [], 0))