'''
15. 3Sum
For example, given array S = [-1, 0, 1, 2, -1, -4], target=0

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

给定一个整型数组num， 找出这个数组中满足这个条件的所有数字： num[i]+num[j]+num[k] = 0. 
题目的两点要求：
1. 每个答案组里面的三个数字是要从大到小排列起来的。
2. 每个答案不可以和其他的答案相同
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenth = len(nums)
        results = []
        nums = sorted(nums)
        
        i=0
        while i < lenth-2:
            left = i+1
            right = lenth-1
            while right>left:
                one = nums[left]
                two = nums[i]
                three = nums[right]
                if one+two+three==0:
                    results.append([two,one,three])
                    left+=1
                    right-=1
                    while left<right and nums[left-1]==nums[left]:
                        left+=1
                    while left<right and nums[right+1]==nums[right]:
                        right-=1
                elif one+two+three<0:
                    left+=1
                else:
                    right-=1
            
            i+=1
            while i<lenth-2 and nums[i-1]==nums[i]:
                i+=1

    



a = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(a.threeSum(nums))