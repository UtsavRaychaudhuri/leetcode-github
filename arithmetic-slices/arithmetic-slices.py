class Solution:
    def numberOfArithmeticSlices(self, a: List[int]) -> int:
        if len(a)<3:
            return 0
        d=a[1]-a[0]
        count=0
        maxcount=0
        for i in range(2,len(a)):
            if a[i]-a[i-1]==d:
                count+=1
                maxcount+=count
            else:
                count=0
                d=a[i]-a[i-1]
        return maxcount
                
            
                
