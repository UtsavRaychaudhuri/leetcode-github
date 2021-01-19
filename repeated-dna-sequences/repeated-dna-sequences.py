class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        my_set=set()
        res=set()
        for i in range(len(s)-9):
            string=s[i:i+10]
            if string in my_set:
                res.add(string)
            else:
                my_set.add(string)
        return list(res)
