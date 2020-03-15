


class MedianFinder:

    def __init__(self):
        self.elements = list()
        self.N = 0

    def addNum(self, num: int) -> None:
        if (self.N == 0 or self.elements[self.N - 1] <= num):
            self.elements.append(num)
            self.N += 1
            return
        self.N += 1
        for index, element in enumerate(self.elements):
            if (num < element):
                old_elements = self.elements[:]
                self.elements = list()
                for i in range(index):
                    self.elements.append(old_elements[i])
                self.elements.append(num)
                for i in range(index, self.N - 1):
                    self.elements.append(old_elements[i])
                break

    def findMedian(self) -> float:
        if (self.N % 2 == 1):
            return self.elements[self.N // 2]
        return (self.elements[self.N // 2] + self.elements[self.N // 2 - 1]) / 2



def main():
    median = MedianFinder()
    median.addNum(1)
    median.addNum(3)
    median.addNum(2)
    median.addNum(2)
    median.addNum(0)
    print(median.findMedian())



if __name__ == "__main__":
    main()