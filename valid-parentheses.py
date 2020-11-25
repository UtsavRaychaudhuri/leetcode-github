class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_stack=[]
        for i in s:
            if i==')' or i=='}' or i==']':
                if len(my_stack)==0:
                    return False
                popped_element=my_stack.pop()
                if ( i==')' and popped_element != '(' ) or ( i== '}' and popped_element !='{' ) or ( i==']' and popped_element != '[' ) :
                    return False
                continue
            my_stack.append(i)
        return len(my_stack)==0
            
        
