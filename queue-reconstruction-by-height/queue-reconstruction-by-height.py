class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def sort_people(a,b):
            if (a[0]==b[0] and a[1]<b[1]) or a[0]>b[0]:
                return -1
            return 1
        people=sorted(people,key=functools.cmp_to_key(sort_people))
        res=[]
        for i,j in people:
            if j>=len(res):
                res.append([i,j])
            else:
                res.insert(j,[i,j])
        return res
