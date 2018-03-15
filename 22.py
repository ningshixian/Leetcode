class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        else:
            ans = []
            self.dfs(n, n, ans, '')
            return ans
    
    def dfs(self, left, right, ans, s):
        if left>right:
            return
        if not left and not right:
            ans.append(s)
            return
        if left:
            self.dfs(left-1, right, ans, s+'(')
        if right>left:
            self.dfs(left, right-1, ans, s+')')
 
a = Solution()
n=3
print(a.generateParenthesis(n))