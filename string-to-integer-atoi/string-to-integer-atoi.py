class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        neg=False
        digit=0
        for i in range(len(s)):
            if i==0 and s[i] in {'-','+'}:
                if s[i]=='-':
                    neg=True
                continue
            if not s[i].isdigit():
                break
            else:
                digit=digit*10+int(s[i])
        if neg:
            digit=-digit
            if digit<-2147483648:
                return -2147483648
            return digit
        if digit>2147483647:
            return 2147483647
        return digit
            