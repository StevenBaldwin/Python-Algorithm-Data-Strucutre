from random import randint
import sys

def closest_pairs(arr,val):
    left_idx,right_idx = -1,-1
    min_diff = float('inf')
    l = 0
    h = len(arr)-1

    while l<h:
        if abs(arr[l]+arr[h]-val) < min_diff:
            left_idx = l
            right_idx = h
            min_diff =abs(arr[l]+arr[h]-val)
        elif (arr[l]+arr[h]) <val:
            l+=1
        else:
            h-=1
    return (left_idx,right_idx)



def brute_force(arr,val):
    l,r=-1,-1
    min_diff = float('inf')
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if abs(arr[i]+arr[j]-val)<min_diff:
                min_diff =abs(arr[i]+arr[j]-val)
                l=i
                r=j
    return (l,r)


def tester():
    for g in range(10):
        arr = [randint(1,10000) for i in range(1000)]
        arr.sort()
        val = randint(2,20000)
        if closest_pairs(arr,val)!=brute_force(arr,val):
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
