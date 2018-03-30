'''
9. Palindrome Number
题目翻译: 给定一个数字， 要求判断这个数字是否为回文数字. 

比如121就是回文数字， 122就不是回文数字.

'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0:
            return False
        if len(str(x))==1:
            return True
        elif len(str(x))==2:
            if str(x)[0]==str(x)[1]:
                return True
            else:
                return False
        i = 0
        flag = True
        x = str(x)
        while i < len(x) / 2:
            if x[i] == x[len(x)-i-1]:
                i += 1
            else:
                flag = False
                break
        return flag



a = Solution()
nums = 1
print(a.isPalindrome((nums)))