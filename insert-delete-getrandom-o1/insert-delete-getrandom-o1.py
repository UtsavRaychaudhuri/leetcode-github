from random import choice
class RandomizedSet:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list=[]
        self.hashmap={}
        
​
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashmap:
            self.list.append(val)
            self.hashmap[val]=len(self.list)-1
            return True
        else:
            return False
            
​
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashmap:
            temp=self.list[-1]
            self.list[-1],self.list[self.hashmap[val]]=self.list[self.hashmap[val]],self.list[-1]
            self.hashmap[temp]=self.hashmap[val]
            self.list.pop()
            del self.hashmap[val]
            return True
        return False
​
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
