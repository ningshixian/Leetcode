'''
191.Number of 1 Bits
题目翻译: 给出一个整数， 求它包含二进制1的位数。 例如， 32位整数 11 的二进制表达形式
是 00000000000000000000000000001011 ， 那么函数应该返回3。

例子
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n//2:
            if n%2==1:
                count+=1
            n = n//2
        if n%2==1:
            count+=1
        return count
            


a = Solution()
n = 11
print(a.hammingWeight(n))