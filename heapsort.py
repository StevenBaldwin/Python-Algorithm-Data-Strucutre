import sys
from random import randint

def heapify(arr,n,i):
    l = 2*i + 1
    r = 2*(i+1)
    largest = i
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)


def heapsort(arr):

    for i in range(len(arr)//2 + 1, -1,-1):
        heapify(arr,len(arr),i)
    for i in range(len(arr)-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
    return arr

def tester():
    for _ in range(10):
        l = [randint(-2**30,2**30) for x in range(1000)]
        correct = sorted(l) == heapsort(l)
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
