            node=self.hashmap[key]
            self.hashmap[key].freq+=1
            freq=self.hashmap[key].freq
            self.removefromfreqmap(node,freq-1)
            self.addtofreqmap(node,freq)
        else:
            return -1
        return self.hashmap[key].value
        
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
            self.minfreq=1
            node=DLL(key,value,1)
            self.addtofreqmap(node=node,freq=freq)
            self.hashmap[key]=node
