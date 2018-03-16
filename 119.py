'''
119. Pascal's Triangle II
不同于上一题， 这里我们仅仅需要得到的第k层的集合， 但只能使用O(k)的空间。 
所以不能用前面二维数组的方式， 只能使用一位数组滚动计算

'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        i=0
        while i<=rowIndex:
            if i==0:
                ans = [1]
            elif i==1:
                ans = [1,1]
            else:
                t = [1] * (i+1)
                for j in range(1, i):
                    t[j] = ans[j-1] + ans[j]
                ans = t
            i+=1
        return ans



a = Solution()
for nums in range(8):
    print(a.getRow(nums))