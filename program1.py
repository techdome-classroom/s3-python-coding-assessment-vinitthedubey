class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_format = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_format:
                top = stack.pop() if stack else '#'
                if bracket_format[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack








    



  

