'''
16. 3Sum Closest
给定一个整形数组S和一个具体的值， 要求找出在这数组中三个元素的和和这个给定的值最小。 input只有
一个有效答案。

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        nums = sorted(nums)
        closest=999999

        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while right>left:
                one = nums[i]
                two = nums[left]
                three = nums[right]
                sum = one + two + three
                diff = abs(sum-target)
                if sum==target:
                    return sum
                if diff<closest:
                    result = sum
                    closest = diff
                if sum>target:
                    right-=1
                else:
                    left+=1
        return result



a = Solution()
nums = [1,2,4,8,16,32,64,128]
target = 82
print(a.threeSumClosest(nums, target))