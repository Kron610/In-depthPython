import collections

class Sequence (list):
    
    def __new__(cls, arg = None):
        if (arg == None):
            return super().__new__(cls)
        if (isinstance(arg, collections.Iterable)):
            for element in arg:
                if (not isinstance(element, int)):
                    raise Exception("Argument contains non integer object")
            return super().__new__(cls)  
        else:
            raise Exception("Argument isn't iterable")
        
    def __add__(self, other):
        if (len(self) < len(other)):
            first = self[:]
            second = other
            while (len(first) < len(second)):
                first.append(0)
        if (len(other) < len(self)):
            first = self
            second = other[:]
            while (len(second) < len(first)):
                second.append(0)
        result = Sequence()
        for i in range(len(first)):
            result.append(first[i] + second[i])
        return result
    
    def __sub__(self, other):
        if (len(self) < len(other)):
            first = self[:]
            second = other
            while (len(first) < len(second)):
                first.append(0)
        if (len(other) < len(self)):
            first = self
            second = other[:]
            while (len(second) < len(first)):
                second.append(0)
        result = Sequence()
        for i in range(len(first)):
            result.append(first[i] - second[i])
        return result
    
    def __lt__(self, other):
        if (sum(self) < sum(other)):
            return True
        return False
    
    def __gt__ (self, other):
        if (sum(self) > sum(other)):
            return True
        return False
    
    def __eq__(self, other):
        if (sum(self) == sum(other)):
            return True
        return False
    
    def __le__(self, other):
        return not (self > other)
    
    def __ge__(self, other):
        return not (self < other)
    
    def __ne__(self, other):
        return not (self == other)
    
    def __setitem__(self, key, value):
        if (not isinstance(value, int)):
            raise Exception("Argument isn't integer")
        super().__setitem__(self, key, value)
        
    def append(self, obj):
        if (not isinstance(obj, int)):
            raise Exception("Argument isn't integer")
        super().append(obj)
    
    def extend(self, iterable):
        if (not isinstance(iterable, collections.Iterable)):
            raise TypeError("{} object is not iterable".format(type(iterable)))
        for element in iterable:
            if (not isinstance(element, int)):
                    raise Exception("Argument contains non integer object")
        super().extend(iterable)
    
    def insert(self, index, obj):
        if (not isinstance(obj, int)):
            raise Exception("Argument isn't integer")
        super().insert(index, obj)

def main():
    a = Sequence()
    a.append(1)
    a.insert(0, 0)
    a.extend([9, 8])
if __name__ == "__main__":
    main()