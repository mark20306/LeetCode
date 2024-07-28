class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.minHeap = []
        self.remove = set()

    def popSmallest(self) -> int:
        if self.minHeap:
            smallest = heapq.heappop(self.minHeap)
            self.remove.add(smallest)
            return smallest
        smallest = self.current
        self.remove.add(smallest)
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.remove:
            heapq.heappush(self.minHeap, num)
            self.remove.remove(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)