class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict=dict()
        for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]].append(i)
            else:
                my_dict[s[i]]=[i]
        keys=list(my_dict.keys())
        res=[]
        return_res=[]
        res.append([my_dict[keys[0]][0],my_dict[keys[0]][-1]])
        for i in range(1,len(keys)):
            if my_dict[keys[i]][0]<res[-1][-1] and my_dict[keys[i]][-1]<res[-1][-1]:
                continue
            elif my_dict[keys[i]][0]<res[-1][-1]:
                res[-1][-1]=my_dict[keys[i]][-1]
            else:
                res.append([my_dict[keys[i]][0],my_dict[keys[i]][-1]])
        for i in res:
            return_res.append(i[-1]-i[0]+1)
            
        return return_res
            
            
            
            
            
        
