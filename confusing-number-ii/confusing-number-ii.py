class Solution:
    def confusingNumberII(self, N: int) -> int:
        options=[0,1,6,8,9]
        self.res=0
        def valid(number):
            maps={"0":"0","1":"1","6":"9","8":"8","9":"6"}
            number=str(number)
            newnumber="".join(maps[i] for i in number)
            if number==newnumber[::-1]:
                return False
            return True
            
            
        def cn(number):
            if number>0 and number<=N and valid(number):
                self.res+=1
            if number>N:
                return
            for i in options:
                number=number*10+i
                if number==0:
                    continue
                cn(number)
                number//=10
        cn(0)
        return self.res

sol=Solution()
sol.confusingNumberII(100)