class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack=[]
        for i in tokens:
            if i=="+" or i=="-" or i=="*" or i=="/":
                second_value=token_stack.pop()
                first_value=token_stack.pop()
                if i=="+":
                    token_stack.append(first_value+second_value)
                if i=="-":
                    token_stack.append(first_value-second_value)
                if i=="*":
                    token_stack.append(first_value*second_value)
                if i=="/":
                    val=first_value/second_value
                    if val<0:
                        token_stack.append(math.ceil(val))
                    else:
                        token_stack.append(math.floor(val))
                        
            else:
                token_stack.append(int(i))
        return token_stack.pop()
                    
