import random

def selection_sort( arr):

    for i in range(len(arr)):
        midx = i

        for j in range(i,len(arr)):
            if arr[j] < arr[midx]:
                midx = j
        if midx != i:
            arr[midx],arr[i] = arr[i],arr[midx]
    return arr


def tester():

    for _ in range(25):
        rand_arr = [random.randint(-10**3,10**3) for i in range(1000)]
        print(sorted(rand_arr) == selection_sort(rand_arr))

tester()
