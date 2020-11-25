class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y= str(x)
        i = len(y)-1
        if x<0:
            string = "-"
            while(i>=1):
                string= string+y[i]
                i-=1
            if int(string)<(-2**31):
                return 0
            return int(string)
        string = ""
        while(i>=0):
            string= string+y[i]
            i-=1
        if int(string)>(2**31-1):
            return 0
        return int(string)
