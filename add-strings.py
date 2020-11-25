class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=""
        carry=0
        if len(num2)>len(num1):
            num1,num2=num2,num1
        for i in range(-1,-len(num1)-1,-1):
            if i>=-len(num2):
                sum=ord(num1[i])-ord('0') + (ord(num2[i])-ord('0'))+carry
            else:
                sum=ord(num1[i])-ord('0')+carry
            carry=sum//10
            res=str(sum%10)+res
        if carry==1:
            return "1"+res
        else:
            return res
            
            
            
