class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        occurences_dict=collections.defaultdict(int)
        for i in range(len(S)):
            occurences_dict[S[i]]=i
        l,r,i=0,0,0
        res=[]
        while(i<=r and r<len(S)):
            r=max(r,occurences_dict[S[i]])
            if i==r:
                res.append(r-l+1)
                l=r+1
                if l<len(S):
                    r=occurences_dict[S[l]]
            i+=1
        return res
            
            
                
            
                
            
