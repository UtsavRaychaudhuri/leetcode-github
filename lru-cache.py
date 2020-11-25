from collections import OrderedDict
​
class LRUCache:
​
    def __init__(self, capacity: int):
        self.my_dict=OrderedDict()
        self.capacity=capacity
        self.capacity_now=0
​
​
    def get(self, key: int) -> int:
        if key in self.my_dict:
            self.my_dict.move_to_end(key)
            return self.my_dict[key]
        else:
            return -1
        
​
    def put(self, key: int, value: int) -> None:
        if self.capacity_now==self.capacity and key not in self.my_dict:
            self.my_dict.popitem(last=False)
            self.capacity_now-=1
        if key in self.my_dict:
            self.my_dict.move_to_end(key)
            self.capacity_now-=1
        self.my_dict[key]=value
        self.capacity_now+=1
        
​
​
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
