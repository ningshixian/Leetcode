'''
74. Search a 2D Matrix

题目翻译: 给定一个矩阵和一个特定值， 要求写出一个高效的算法在这个矩阵中快速的找出是否这个给定的
值存在. 但是这个矩阵有以下特征.
1. 对于每一行， 数值是从左到右从小到大排列的.
2. 对于每一列， 数值是从上到下从小到大排列的.

题目解析: 对于这个给定的矩阵， 我们如果用brute force解法， 用两个嵌套循环， O(n2)便可以得到答案.但
是我们需要注意的是这道题已经给定了这个矩阵的两个特性， 这两个特性对于提高我们算法的时间复杂度
有很大帮助， 首先我们给出一个O(n)的解法， 也就是说我们可以固定住右上角的元素， 根据递增或者递减
的规律， 我们可以判断这个给定的数值是否存在于这个矩阵当中
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            
            # for row in matrix:
            #     if not row:
            #         return False
            #     if target > row[-1]:
            #         continue
            #     elif target < row[-1]:
            #         for lie in row:
            #             if lie==target:
            #                 return True
            #         else:
            #             return False
            #     else:
            #         return True
            # return False
            
            if not matrix:
                return False
            if not matrix[0]:
                return False
            row=0
            col = len(matrix[row])-1
            while row<len(matrix) and col>=0:
                if matrix[row][col]>target:
                    col-=1
                elif matrix[row][col]<target:
                    row+=1
                else:
                    return True
            return False


a = Solution()
nums = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
# nums = [[]]
target = 35
print(a.searchMatrix(nums, target))