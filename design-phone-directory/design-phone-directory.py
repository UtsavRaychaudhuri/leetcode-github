class PhoneDirectory:
​
    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.my_set=set()
        for i in range(maxNumbers):
            self.my_set.add(i)
        
        
​
    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        self.numbertobereleased=None
        if len(self.my_set)==0:
            return -1
        for i in self.my_set:
            self.numbertobereleased=i
            break
        self.my_set.remove(self.numbertobereleased)
        return self.numbertobereleased
        
            
        
​
    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.my_set
        
​
    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.my_set.add(number)
        
​
​
# Your PhoneDirectory object will be instantiated and called as such:
