import math
from random import randint
import sys

class SegmentTree:

    def __init__(self,input_arr):
        self.arr = list(input_arr) #copying
        self.n = len(self.arr)
        height = int(math.ceil(math.log(self.n,2)))

        st_size = 10**5
        self.st = [0]*(st_size)

        # import pdb
        # pdb.set_trace()
        self._build(1, 0, (self.n-1))




    def left(self,n):
        return n*2
    def right(self,n):
        return 2*n + 1

    def _build(self,p,L,R):
        # print(p,L,R)
        if L==R:
            self.st[p] = L
        else:
            self._build(self.left(p),   L,  (L+R)//2)
            self._build(self.right(p),   (L+R)//2 + 1,  R)
            p1 = self.st[self.left(p)]
            p2 = self.st[self.right(p)]
            self.st[p] =  p1 if self.arr[p1] <= self.arr[p2]  else p2

    def rmq_util(self,p,L,R,i,j):
        if (i>R or j <L):
            return -1
        if (L>= i and R <=j):
            return self.st[p]
        p1 = self.rmq_util(self.left(p), L, (L+R)//2 ,i, j)
        p2 = self.rmq_util(self.right(p), (L+R)//2 + 1, R, i, j)

        if p1==-1:
            return p2
        if p2 == -1:
            return p1
        return p1 if self.arr[p1] <= self.arr[p2]  else p2

    def rmq(self,i,j):
        return self.arr[self.rmq_util(1,0,self.n - 1, i,j)]





def tester():
    size = 10000
    rand_arr = [randint(-20,20) for i in range(size)]
    # print(rand_arr)
    sgt = SegmentTree(rand_arr)
    for i in range(10000):
        a = randint(0,size-1)
        b = randint(0,size-1)
        a,b = min(a,b),max(a,b)
        # print("a,b",a,b)
        ans = min(rand_arr[a:b+1])

        correct = sgt.rmq(a,b)==ans
        if not correct:
            print("FAIL")
            sys.exit(0)
    print("""
_____                _____    _____   ______   _____        _     _     _
|  __ \      /\      / ____|  / ____| |  ____| |  __ \      | |   | |   | |
| |__) |    /  \    | (___   | (___   | |__    | |  | |     | |   | |   | |
|  ___/    / /\ \    \___ \   \___ \  |  __|   | |  | |     | |   | |   | |
| |       / ____ \   ____) |  ____) | | |____  | |__| |     |_|   |_|   |_|
|_|      /_/    \_\ |_____/  |_____/  |______| |_____/      (_)   (_)   (_)
""")
tester()
