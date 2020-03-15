from collections import deque
from time import time

class ICache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.size = 0
        self.time = dict()
        self._dict = dict()     

    def get_value(self, key: str) -> str:
        self.time[key] = time()
        if (self._dict[key] == None):
            return ''
        return self._dict[key]

    def set_value(self, key: str, value: str) -> None:
        if (self.size < self.capacity):
            self._dict[key] = value
            self.size += 1
            self.time[key] = time()
            return
        min_key = list(sum(sorted(self.time.items(), key = lambda x:x[1]), ()))[0]
        self._dict[min_key] = None
        self._dict[key] = value
        self.time[min_key] = None
        self.time[key] = time()

    def del_value(self, key: str) -> None:
        if (self._dict[key] == None):
            return
        self.time[key] = None
        self._dict[key] = None
        self.size -= 1




def main():
    cache = ICache(2)
    cache.set_value('Jesse', 'Pinkman')
    cache.set_value('Walter', 'White')
    cache.set_value('Juicy', 'James')
    print(cache.get_value('Jesse')) 
    cache.del_value('Walter')
    print(cache.get_value('Walter')) 

if __name__ == "__main__":
    main()