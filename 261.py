'''
231. Power of Two
题目翻译: 给出一个整数， 判断它是否是2的幂。
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        if not n==1 and n%2==1:
            return False
        while n%2==0:
            n=n/2
        if n==1:
            return True
        else:
            return False


a = Solution()
nums = 13
print(a.isPowerOfTwo(nums))