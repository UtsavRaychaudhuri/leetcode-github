class Solution:
    def expand(self, S: str) -> List[str]:
        final_stack=[]
        i=0
        while(i<len(S)):
            if S[i]=='{':
                i+=1
                local_stack=[]
                while(S[i]!='}'):
                    if S[i].isalpha():
                        local_stack.append(S[i])
                    i+=1
                final_stack.append(local_stack)
            elif S[i].isalpha():
                final_stack.append([S[i]])
            i+=1
            
        def backtrack(final_stack,index,res):
            if index==len(final_stack):
                self.final_res.append("".join(res))
                return
            for i in final_stack[index]:
                res.append(i)
                backtrack(final_stack,index+1,res)
                res.pop()
        
        self.final_res=[]
        backtrack(final_stack,0,[])
        return sorted(self.final_res)
        
            
                
                
                
            
                
                
