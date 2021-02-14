class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        arr=[i for i in range(len(M))]
        rank=[1]*len(M)
        def find(x):
            if arr[x]!=x:
                arr[x]=find(arr[x])
            return arr[x]
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j]==1 and i!=j:
                    if find(arr[i])!=find(arr[j]):
                        arr[find(i)]=find(arr[j])
        res=len(set(find(i) for i in arr))
        return res