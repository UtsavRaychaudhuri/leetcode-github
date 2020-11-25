class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        my_dict=dict()
        j=0
        for i in order:
            my_dict[i]=j
            j+=1
        k=0
        i=0
        while(i<len(words)):
            if i+1==len(words):
                break
            if (k==len(words[i]) and k==len(words[i+1])) or (k==len(words[i]) and k<len(words[i+1])):
                i+=1
                continue
            elif k==len(words[i+1]) and k<len(words[i]):
                return False
            if my_dict[words[i][k]]<my_dict[words[i+1][k]]:
                i+=1
            elif my_dict[words[i][k]]==my_dict[words[i+1][k]]:
                k+=1
            else:
                return False
        return True
