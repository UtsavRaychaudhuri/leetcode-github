class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temperatures_stack=[[T[0],0]]
        res=[0]*len(T)
        for i in range(1,len(T)):
            while temperatures_stack and T[i]>temperatures_stack[-1][0]:
                    res[temperatures_stack[-1][1]]=i-temperatures_stack[-1][1]
                    temperatures_stack.pop()
            temperatures_stack.append([T[i],i])
        return res
                
                
                
            
