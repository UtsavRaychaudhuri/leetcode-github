# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
​
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=0
        h=n-1
        while(l<=h):
            m=(l+h)>>1
            if isBadVersion(m):
                h=m-1
            else:
                l=m+1
        return l
        
