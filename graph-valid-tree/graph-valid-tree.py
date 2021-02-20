import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=[i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        for i,v in edges:
            parent_i=find(i)
            parent_v=find(v)
            if parent_i==parent_v:
                return False
            parent[parent_i]=parent[parent_v]
        return len(set(find(i) for i in range(n)))==1
            
            
            
        