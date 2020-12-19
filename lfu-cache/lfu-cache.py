        tail=self.freqmap[freq][1]
        if head.next==tail:
            del self.freqmap[freq]
            if freq==self.minfreq:
                self.minfreq+=1
​
    def addtofreqmap(self,node,freq):
        if freq not in self.freqmap:
            self.freqmap[freq]=self.createDLL()
        head=self.freqmap[freq][0]
        self.appendtoDLL(head,node)
​
        
​
    def get(self, key: int) -> int:
        if key in self.hashmap:
            node=self.hashmap[key]
            self.hashmap[key].freq+=1
            freq=self.hashmap[key].freq
            self.removefromfreqmap(node,freq-1)
            self.addtofreqmap(node,freq)
            return self.hashmap[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return
        # if key is in hashmap
        if len(self.hashmap)==self.capacity and key not in self.hashmap:
            tail=self.freqmap[self.minfreq][1]
            head=self.freqmap[self.minfreq][1]
            del self.hashmap[tail.prev.key]
            self.removefromendDLL(tail)
            if head.next==tail:
                del self.freqmap[self.minfreq]
            
        if key in self.hashmap:
            self.hashmap[key].freq+=1
            self.hashmap[key].value=value
            freq=self.hashmap[key].freq
            self.removefromfreqmap(self.hashmap[key],freq-1)
            self.addtofreqmap(self.hashmap[key],freq)
        else:
            freq=1
