'''
118. Pascal's Triangle
要得到一个帕斯卡三角

For example, given numRows = 5, Return
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]

1、第k层有k个元素
2、每层第一个以及最后一个元素值为1
3、对于第k（ k > 2） 层第n（ n > 1 && n < k） 个元素A[k][n]， A[k][n] = A[k-1][n-1] + A[k-1][n]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        ans = []
        for i in range(numRows):
            if i==0:
                ans.append([1])
            elif i==1:
                ans.append([1,1])
            else:
                t = [1] * (i+1)
                for j in range(1, i):
                    t[j] = ans[i-1][j-1] + ans[i-1][j]
                ans.append(t)
        return ans



a = Solution()
for nums in range(8):
    print(a.generate(nums))