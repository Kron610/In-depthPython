
from typing import List
class MaxHeap:
    def __init__(self) -> None:
        self.elements = list()
        self.N = 0
        self.elements.append(0)
    
    def __swim(self, key: int) -> None:
        while (key > 1 and self.elements[key // 2] < self.elements[key]):
            cash = self.elements[key // 2]
            self.elements[key // 2] = self.elements[key]
            self.elements[key] = cash
            key //= 2
    
    def __sink(self, key: int) -> None:
        while (2 * key <= self.N):
            j = 2 * key
            if (j < self.N and self.elements[j] < self.elements[j+1]):
                j += 1
            if (self.elements[key] >= self.elements[j]):
                break
            cash = self.elements[key]
            self.elements[key] = self.elements[j]
            self.elements[j] = cash
            key = j

    def push(self, val: int) -> None:
        self.N += 1
        self.elements.append(val)
        self.__swim(self.N)



    def pop(self) -> int:
        max_ = self.elements[1]
        self.elements[1] = self.elements[self.N]
        self.N -= 1
        self.__sink(1)
        self.elements.pop()
        return max_

    def heapify(self, iterable: List[int]) -> None:
        self.elements = list()
        self.elements.append(0)
        for element in iterable:
            self.push(element)




def main():
    heap = MaxHeap()
    a = [1, 3, 5, 9 ,2]
    heap.heapify(a)
    print(heap.pop())
    heap.push(15)
    print(heap.pop())


if __name__ == "__main__":
    main()