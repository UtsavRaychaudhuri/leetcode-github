class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections=sorted(connections,key=lambda x:x[2])
        arr=[i for i in range(N+1)]
        rank=[1]*(N+1)
        components = N
        def union_find(x,y):
            arr[y]=find(arr[x])
        def find(x):
            if x==arr[x]:
                return x
            root=find(arr[x])
            arr[x]=root
            return root
        cost=0
        for x,y,z in connections:
            root_x, root_y = find(x), find(y)
            if root_x!=root_y:
                if rank[root_y]>rank[root_x]:
                    root_x, root_y = root_y, root_x
                cost+=z
                arr[root_y]=root_x
                rank[root_x]+=rank[root_y]
                rank[root_x]=rank[root_x]
                components -= 1
                if components == 1:
                    return cost
        return -1