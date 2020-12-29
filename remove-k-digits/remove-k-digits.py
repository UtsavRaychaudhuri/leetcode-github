class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digit_stack=[]
        for i in num:
            while k and digit_stack and i<digit_stack[-1] :
                digit_stack.pop()
                k-=1
            digit_stack.append(i)
        if k>0:
            number="".join(digit_stack[:len(digit_stack)-k])
            if number=="":
                return "0"
            return str(int(number))
        return str(int("".join(digit_stack)))
                
        
        
            
            
