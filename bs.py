from random import randint
import sys


def binary_search(arr,i):
    l = 0
    h = len(arr)-1

    while l<=h:
        mid = (l+h)//2

        if arr[mid] < i:
            l=mid+1
        elif arr[mid]==i:
            return mid
        else:
            h = mid-1
    return -1



def tester():
    t_s = {randint(-2**50,2**50) for i in range(15000)}
    s_l = sorted(list(t_s))
    for i in t_s:
        correct = s_l.index(i) == binary_search(s_l,i)
        if not correct:
            print("FAILED!")
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
