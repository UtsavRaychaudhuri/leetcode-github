import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False
        parent=[i for i in range(n)]
        size=[1]*n
        def find(x):
            root=x
            while parent[root]!=root:
                root =parent[root]
            while x!=root:
                old=parent[x]
                parent[x]=root
                x=old
            return root
        for e1,e2 in edges:
            parent1=find(e1)
            parent2=find(e2)
            if parent1==parent2:
                return False     
            if size[parent1]<size[parent2]:
                parent[parent1]=parent2
                size[parent2]+=size[parent1]
            else:
                parent[parent2]=parent1
                size[parent1]+=size[parent2]
        return True
            
            
            
        