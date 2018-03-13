class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a, b, c= 0, 0, 0
        # brackets = ['(', ')', '{', '}', '[', ']']
        # if len(s)%2==1:
        #     return False
        # for char in s:
        #     if char=='(':
        #         a+=1
        #     elif char==')':
        #         a-=1
        #     elif char=='{':
        #         b+=1
        #     elif char=='}':
        #         b-=1
        #     elif char=='[':
        #         c+=1
        #     elif char==']':
        #         c-=1
        #     else:
        #         return False
        # if a==0 and b==0 and c==0:
        #     return True
        # else:
        #     return False

        if len(s)%2==1:
            return False
        brackets = ['(', ')', '{', '}', '[', ']']
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if (char==')' and stack[-1]=='(') or (char==']' and stack[-1]=='[') or (char=='}' and stack[-1]=='{'):
                    stack.pop()
                else:
                    stack.append(char)
        if stack:
            return False
        else:
            return True

a = Solution()
s = "([]){[}]"
print(a.isValid(s))