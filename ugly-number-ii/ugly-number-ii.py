class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res=[1]
        i,j,k=0,0,0
        while(len(res)<n):
            num=min(2*res[i],3*res[j],5*res[k])
            if num>res[-1]:
                res.append(num)
            if 2*res[i]==num:
                i+=1
            if 3*res[j]==num:
                j+=1
            if 5*res[k]==num:
                k+=1
        return res[-1]
                