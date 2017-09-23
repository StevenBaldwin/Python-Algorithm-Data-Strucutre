import random

class MaxHeap:

    def __init__(self, arg):
        self.arr = arg
        self._build_heap()

    def _build_heap(self):
        for i in range((len(self.arr)-1),-1,-1):
            self.heapify(i)


    def heapify(self,i):
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        n = len(self.arr)
        if l < n and self.arr[l] > self.arr[largest]:
            largest = l
        if r < n and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            self.arr[largest],self.arr[i] = self.arr[i],self.arr[largest]
            self.heapify(largest)

    def insert(self,key):
        self.arr.append(None)
        i = len(self.arr) -1
        parent = (i-1)//2

        while i > 0 and self.arr[parent] < key:
            self.arr[parent],self.arr[i] = self.arr[i],self.arr[parent]
            i = parent
            parent = (i-1)//2
        self.arr[i] = key


    def extract_max(self):
        mx = self.arr[0]
        if len(self.arr) > 1:
            self.arr[0] = self.arr.pop()
            self.heapify(0)
        else:
            self.arr.pop()
        return mx        


def test_heap():
    arr = [random.randint(2,500) for x in range(20)]

    hep = MaxHeap(list(arr))
    for _ in range(20):
        t = random.randint(2,500)
        arr.append(t)
        hep.insert(t)

    arr.sort()
    arr = list(reversed(arr))

    print(arr)
    print(hep.arr)
    for i in range(len(arr)):
        if arr[i] != hep.extract_max():
            return False

    return True


print(test_heap())
