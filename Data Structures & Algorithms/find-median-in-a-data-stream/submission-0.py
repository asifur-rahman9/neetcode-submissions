class MedianFinder:

    def __init__(self):
        self.nums = []

        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        index = n // 2
        
        if n % 2 == 0:
            return (self.nums[index - 1] + self.nums[index]) / 2.0
        else:
            return float(self.nums[index])
            
        
        