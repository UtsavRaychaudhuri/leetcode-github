class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a=A[0]
        b=B[0]
        def check(a):
            check=0
            check1=0
            for i in range(len(A)):
                if a not in (A[i],B[i]):
                    return -1
                elif a!=B[i]:
                    check+=1
                elif a!=A[i]:
                    check1+=1
            return min(check,check1)
        checka=check(a)
        checkb=check(b)
        if checka==-1 and checkb==-1:
            return -1
        if checka==-1:
            return checkb
        return checka
    
        
                
                
                
                
                
                
