class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i=0
        j=0
        seqs=0
        elementsmatched=0
        while(j<len(target)):
            if source[i]==target[j]:
                elementsmatched+=1
                j+=1
            i+=1
            if i==len(source):
                seqs+=1
                if elementsmatched==0:
                    return -1
                elementsmatched=0
                i=0
        if i>0:
            return seqs+1
        return seqs
        
            
            
