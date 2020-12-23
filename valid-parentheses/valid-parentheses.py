class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_stack=[]
        for i in s:
            if i==")" and len(my_stack)>0 and my_stack[-1]=='(':
                my_stack.pop()
            elif i=='}' and len(my_stack)>0 and my_stack[-1]=='{':
                my_stack.pop()
            elif i==']' and len(my_stack)>0 and my_stack[-1]=='[':
                my_stack.pop()
            elif i=='(' or i=='{' or i=='[':
                my_stack.append(i)
            else:
                return False
        if len(my_stack)==0:
            return True
        else:
            return False
                
            
        
